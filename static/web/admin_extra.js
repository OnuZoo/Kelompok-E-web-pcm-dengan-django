/* Interaksi admin PCM Baki: dropdown akun, animasi scroll, bantuan form */
document.documentElement.classList.add('pcm-js');

document.addEventListener('DOMContentLoaded', function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1) Info pengguna menjadi satu tombol dropdown ---------- */
  var ut = document.getElementById('user-tools');
  if (ut) {
    var nameEl = ut.querySelector('strong');
    var nodes = Array.prototype.slice.call(ut.querySelectorAll('a, form'));
    if (nodes.length) {
      var wrap = document.createElement('div');
      wrap.className = 'pcm-user';
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'pcm-user-btn';
      btn.setAttribute('aria-haspopup', 'true');
      btn.setAttribute('aria-expanded', 'false');
      var userName = nameEl ? nameEl.textContent.trim() : 'Akun';
      btn.setAttribute('aria-label', 'Menu akun ' + userName);
      btn.innerHTML = '<span></span><span></span><span></span>';
      var menu = document.createElement('ul');
      menu.className = 'pcm-user-menu';
      nodes.forEach(function (n) {
        var li = document.createElement('li');
        li.appendChild(n);
        menu.appendChild(li);
      });
      ut.textContent = '';
      wrap.appendChild(btn);
      wrap.appendChild(menu);
      ut.appendChild(wrap);

      var setOpen = function (open) {
        wrap.classList.toggle('open', open);
        btn.setAttribute('aria-expanded', String(open));
      };
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        setOpen(!wrap.classList.contains('open'));
      });
      document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) setOpen(false); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
    }
  }

  /* ---------- 2) Animasi muncul saat di-scroll ---------- */
  if ('IntersectionObserver' in window && !reduce) {
    var targets = document.querySelectorAll('#content .module, #content-related, body.dashboard .module tr');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        io.unobserve(el);
        el.classList.add('animasi-tampil');
        var wait = parseFloat(el.style.transitionDelay || '0') * 1000;
        setTimeout(function () {                     // cabut agar efek hover normal kembali
          el.classList.remove('animasi-siap', 'animasi-tampil');
          el.style.transitionDelay = '';
        }, 700 + wait);
      });
    }, { threshold: 0.08 });

    targets.forEach(function (el) {
      el.classList.add('animasi-siap');
      if (el.tagName === 'TR') {                     // kartu muncul satu per satu
        var idx = Array.prototype.indexOf.call(el.parentNode.children, el);
        el.style.transitionDelay = ((idx % 6) * 0.07) + 's';
      }
      io.observe(el);
    });
  }

  /* ---------- 3) Pesan sukses hilang sendiri ---------- */
  document.querySelectorAll('ul.messagelist li').forEach(function (li) {
    setTimeout(function () {
      li.classList.add('pcm-hide');
      setTimeout(function () { li.remove(); }, 600);
    }, 5000);
  });

  /* ---------- 4) Penghitung karakter ---------- */
  document.querySelectorAll('#content-main textarea').forEach(function (ta) {
    var info = document.createElement('div');
    info.className = 'pcm-counter';
    ta.insertAdjacentElement('afterend', info);
    var update = function () { info.textContent = ta.value.length + ' karakter'; };
    ta.addEventListener('input', update);
    update();
  });

  /* ---------- 5) Pratinjau gambar ---------- */
  document.querySelectorAll('input[type=file]').forEach(function (input) {
    input.addEventListener('change', function () {
      var old = input.parentElement.querySelector('.pcm-preview');
      if (old) old.remove();
      var file = input.files && input.files[0];
      if (!file || file.type.indexOf('image/') !== 0) return;
      var img = document.createElement('img');
      img.className = 'pcm-preview';
      img.alt = 'Pratinjau';
      img.src = URL.createObjectURL(file);
      input.insertAdjacentElement('afterend', img);
    });
  });

  /* ---------- 6) Form: peringatan, Ctrl+S, garis loading ---------- */
  var form = document.querySelector('#content-main form[method="post"]');
  var row = document.querySelector('.submit-row');
  if (!form || !row) return;

  var dirty = false;
  form.addEventListener('input', function () { dirty = true; document.body.classList.add('pcm-dirty'); });
  form.addEventListener('submit', function () { dirty = false; document.body.classList.add('pcm-saving'); });
  window.addEventListener('beforeunload', function (e) { if (dirty) { e.preventDefault(); e.returnValue = ''; } });

  var hint = document.createElement('span');
  hint.className = 'pcm-hint';
  hint.textContent = 'Tips: tekan Ctrl+S untuk menyimpan';
  row.appendChild(hint);

  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') {
      e.preventDefault();
      var btn = row.querySelector('input[name="_continue"]') || row.querySelector('input[type=submit]');
      if (btn) btn.click();
    }
  });
});