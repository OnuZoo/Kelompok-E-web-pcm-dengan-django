/* Skrip tambahan admin PCM Baki.
   Dimuat dari templates/admin/base_site.html. */
document.addEventListener("DOMContentLoaded", function () {

  /* Notifikasi hilang sendiri setelah beberapa detik */
  document.querySelectorAll("ul.messagelist li").forEach(function (li, i) {
    setTimeout(function () {
      li.classList.add("pcm-hide");
      setTimeout(function () { li.remove(); }, 500);
    }, 4000 + i * 500);
  });

  /* Selebihnya hanya untuk form tambah/ubah data */
  var form = document.querySelector("#content-main form[id$='_form']");
  if (!form) return;

  /* Penanda perubahan belum disimpan */
  function peringatan(e) {
    if (document.body.classList.contains("pcm-dirty")) {
      e.preventDefault();
      e.returnValue = "";
    }
  }
  form.addEventListener("input", function () {
    document.body.classList.add("pcm-dirty");
  });
  form.addEventListener("submit", function () {
    window.removeEventListener("beforeunload", peringatan);
  });
  window.addEventListener("beforeunload", peringatan);

  /* Pratinjau gambar yang baru dipilih */
  form.querySelectorAll("input[type=file]").forEach(function (input) {
    var img = document.createElement("img");
    img.className = "pcm-preview";
    img.alt = "Pratinjau";
    img.style.display = "none";
    input.insertAdjacentElement("afterend", img);

    input.addEventListener("change", function () {
      var file = input.files && input.files[0];
      if (file && file.type.indexOf("image/") === 0) {
        img.src = URL.createObjectURL(file);
        img.style.display = "block";
      } else {
        img.style.display = "none";
      }
    });
  });
});
