/* ============================================
   animasi.js
   1. Fade in saat di-scroll
   2. Angka berputar acak lalu berhenti di nilai asli
   Tempatkan di: static/web/animasi.js
   ============================================ */
(function () {
  'use strict';

  // Hormati pengguna yang mematikan animasi di perangkatnya
  var kurangGerak = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (kurangGerak || !('IntersectionObserver' in window)) return;

  /* ---------- Daftar elemen yang di-fade in ----------
     Tambah class baru di sini kalau ada halaman lain. */
  var DAFTAR_FADE = [
    '.card',
    '.beranda-hero',
    '.beranda-judul-seksi',
    '.beranda-agenda-item',
    '.pimpinan-kartu',
    '.amal-bidang-header',
    '.amal-kartu',
    '.ranting-kartu',
    '.agenda-item',
    '.berita-utama',
    '.berita-kartu',
    '.profil-timeline-item',
    '.kontak-sekretariat',
    '.unduhan-kartu',
    '.kontak-sekretariat',
    '.kontak-formulir'
  ].join(',');

  /* ---------- Daftar angka yang berputar ---------- */
  var DAFTAR_ANGKA = '.beranda-stat-angka, [data-angka]';

  var KELAS_TUNDA = [
    'animasi-tunda-1', 'animasi-tunda-2', 'animasi-tunda-3',
    'animasi-tunda-4', 'animasi-tunda-5'
  ];

  /* ---------- 1. FADE IN ---------- */
  function urutanDalamInduk(el) {
    var induk = el.parentNode;
    // Kalau kartu dibungkus kolom sendiri-sendiri, pakai urutan kolomnya
    if (induk && induk.children.length === 1 && induk.parentNode) {
      el = induk;
      induk = induk.parentNode;
    }
    return Array.prototype.indexOf.call(induk.children, el);
  }

  function siapkanFade() {
    var semua = document.querySelectorAll(DAFTAR_FADE);

    var pengamat = new IntersectionObserver(function (daftar) {
      daftar.forEach(function (entri) {
        if (!entri.isIntersecting) return;
        var el = entri.target;
        pengamat.unobserve(el);
        el.classList.add('animasi-tampil');

        // Setelah selesai, cabut semua class supaya efek hover asli kembali normal
        setTimeout(function () {
          el.classList.remove.apply(
            el.classList,
            ['animasi-siap', 'animasi-tampil'].concat(KELAS_TUNDA)
          );
        }, 1300);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

    Array.prototype.forEach.call(semua, function (el) {
      // Lewati elemen yang induknya sudah ikut dianimasikan
      if (el.parentNode && el.parentNode.closest(DAFTAR_FADE)) return;

      var urutan = urutanDalamInduk(el) % (KELAS_TUNDA.length + 1);
      el.classList.add('animasi-siap');
      if (urutan > 0) el.classList.add(KELAS_TUNDA[urutan - 1]);
      pengamat.observe(el);
    });
  }

  /* ---------- 2. ANGKA ACAK ---------- */
  // Digit dikunci dari kiri ke kanan, sisanya masih acak.
  function putarAngka(el) {
    var asli = el.textContent;
    var jumlahDigit = (asli.match(/\d/g) || []).length;
    if (!jumlahDigit) return;

    var durasi = Math.min(900 + jumlahDigit * 300, 2200);
    var mulai = null;
    var terakhir = 0;

    el.setAttribute('aria-label', asli.trim());

    function langkah(waktu) {
      if (mulai === null) mulai = waktu;
      var lalu = waktu - mulai;

      if (lalu >= durasi) {
        el.textContent = asli;
        return;
      }

      if (waktu - terakhir >= 60) {
        terakhir = waktu;
        var terkunci = Math.floor((lalu / durasi) * jumlahDigit);
        var urut = 0;
        el.textContent = asli.replace(/\d/g, function (digit) {
          var hasil = urut < terkunci ? digit : String(Math.floor(Math.random() * 10));
          urut++;
          return hasil;
        });
      }
      requestAnimationFrame(langkah);
    }
    requestAnimationFrame(langkah);
  }

  function siapkanAngka() {
    var semua = document.querySelectorAll(DAFTAR_ANGKA);
    if (!semua.length) return;

    var pengamat = new IntersectionObserver(function (daftar) {
      daftar.forEach(function (entri) {
        if (!entri.isIntersecting) return;
        pengamat.unobserve(entri.target);
        putarAngka(entri.target);
      });
    }, { threshold: 0.6 });

    Array.prototype.forEach.call(semua, function (el) {
      pengamat.observe(el);
    });
  }

  function mulai() {
    siapkanFade();
    siapkanAngka();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mulai);
  } else {
    mulai();
  }
})();
