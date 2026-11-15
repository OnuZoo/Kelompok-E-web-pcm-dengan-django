/* =========================================================
   TAMBAHAN TEMA ADMIN PCM BAKI (dimuat SETELAH admin_custom.css)
   ========================================================= */

/* ---------- Logo di samping judul ---------- */
#site-name::before { content: none !important; }   /* matikan lingkaran "PCM" lama */
#site-name a { display: inline-flex; align-items: center; gap: 12px; }
.pcm-logo {
  height: 44px; width: 44px; object-fit: contain;   /* ubah ukuran logo di sini */
  background: #fff; border-radius: 50%; padding: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,.2);
  transition: transform .3s;
}
#site-name a:hover .pcm-logo { transform: rotate(-8deg) scale(1.08); }

/* ---------- Animasi masuk ---------- */
@keyframes pcmUp { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }

/* =========================================================
   DASBOR: model tampil sebagai kartu berikon
   ========================================================= */
body.dashboard #content-main .module { padding-bottom: 6px; }
body.dashboard .module table,
body.dashboard .module tbody { display: block; width: 100%; }
body.dashboard .module caption { display: block; text-align: left; }
body.dashboard .module tbody {
  display: grid; gap: 14px; padding: 16px;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
}
body.dashboard .module tr {
  display: grid; grid-template-columns: 1fr 1fr; gap: 8px; align-content: start;
  background: var(--darkened-bg); border: 1px solid var(--border-color);
  border-radius: 16px; padding: 14px;
  animation: pcmUp .45s ease both;
  transition: transform .2s, box-shadow .2s, border-color .2s;
}
body.dashboard .module tr:hover {
  transform: translateY(-4px); border-color: var(--pcm-primary);
  box-shadow: 0 10px 24px rgba(15,122,74,.18); background: var(--module-bg);
}
body.dashboard .module tr:nth-child(2) { animation-delay: .05s; }
body.dashboard .module tr:nth-child(3) { animation-delay: .1s; }
body.dashboard .module tr:nth-child(4) { animation-delay: .15s; }
body.dashboard .module tr:nth-child(5) { animation-delay: .2s; }
body.dashboard .module tr:nth-child(6) { animation-delay: .25s; }
body.dashboard .module tr:nth-child(n+7) { animation-delay: .3s; }
body.dashboard .module th { grid-column: 1 / -1; padding: 0; border: 0; background: none; }
body.dashboard .module td { padding: 0; border: 0; text-align: center; }
body.dashboard .module th a {
  display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 600;
}
body.dashboard .module td a { display: block; font-size: 12px; font-weight: 500; }
body.dashboard .module td a.addlink { background: var(--pcm-primary); color: #fff; }
body.dashboard .module td a.addlink:hover { background: var(--pcm-primary-dark); }
body.dashboard .module td a.changelink { background: var(--module-bg); border: 1px solid var(--border-color); }


/* =========================================================
   FORM INPUT DATA
   ========================================================= */
#content-main form fieldset.module { animation: pcmUp .4s ease both; margin-bottom: 22px; }
fieldset.module h2 { display: flex; align-items: center; gap: 8px; }

/* baris isian: menyala saat sedang diisi */
.form-row {
  padding: 14px 20px; border-left: 4px solid transparent;
  transition: background .2s, border-color .2s;
}
.form-row:focus-within {
  background: color-mix(in srgb, var(--pcm-primary) 7%, transparent);
  border-left-color: var(--pcm-accent);
}
.form-row label { font-weight: 600; font-size: 13px; color: var(--body-fg); }
.form-row label.required::after { content: " *"; color: #e5484d; }   /* tanda wajib diisi */
.form-row .help, .help { color: var(--body-quiet-color); font-size: 12px; margin-top: 6px; }
.form-row .errorlist { margin-top: 6px; }
.form-row.errors { border-left-color: #e5484d; background: rgba(229,72,77,.07); }

input[type=text], input[type=url], input[type=email], input[type=number],
input[type=password], textarea, select { width: min(100%, 640px); box-sizing: border-box; }
textarea { min-height: 120px; resize: vertical; }
.vLargeTextField, .vTextField { width: min(100%, 640px) !important; }

/* penghitung karakter */
.pcm-counter { font-size: 11px; color: var(--body-quiet-color); margin-top: 4px; }

/* pratinjau gambar */
.pcm-preview {
  display: block; margin-top: 10px; max-width: 220px; max-height: 160px;
  border-radius: 14px; border: 3px solid var(--pcm-accent);
  box-shadow: var(--pcm-shadow); animation: pcmUp .3s ease;
}
input[type=file] {
  padding: 10px; border: 2px dashed var(--pcm-primary); border-radius: 14px;
  background: var(--darkened-bg); width: min(100%, 640px); box-sizing: border-box; cursor: pointer;
}
input[type=file]::file-selector-button {
  border: 0; border-radius: 999px; padding: 7px 16px; margin-right: 12px;
  background: var(--pcm-primary); color: #fff; cursor: pointer; font-family: var(--pcm-font);
}

/* tombol simpan melayang di bawah layar */
.submit-row {
  position: sticky; bottom: 14px; z-index: 20; margin: 24px 0 0;
  display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
  background: var(--module-bg); border: 1px solid var(--border-color);
  box-shadow: 0 8px 28px rgba(0,0,0,.18); padding: 12px 18px;
}
.submit-row input[type=submit].default { background: var(--pcm-primary); }
.submit-row .deletelink { border-radius: 999px; padding: 9px 18px; }
.pcm-hint { margin-left: auto; font-size: 11px; color: var(--body-quiet-color); }

/* penanda perubahan belum disimpan */
body.pcm-dirty .submit-row { border-color: var(--pcm-accent); }
body.pcm-dirty .submit-row::before {
  content: "Ada perubahan belum disimpan"; color: #b88a00; font-size: 12px; font-weight: 600;
}

/* ---------- Pesan (toast) ---------- */
ul.messagelist { position: fixed; top: 80px; right: 24px; z-index: 100; width: min(360px, 90vw); margin: 0; padding: 0; }
ul.messagelist li {
  margin: 0 0 10px; box-shadow: 0 8px 24px rgba(0,0,0,.2);
  animation: pcmUp .35s ease; transition: opacity .5s, transform .5s;
}
ul.messagelist li.pcm-hide { opacity: 0; transform: translateX(30px); }

/* ---------- Daftar data ---------- */
#changelist table tbody tr { transition: background .15s, transform .15s; }
#changelist table tbody tr:hover { background: var(--darkened-bg); }
#searchbar { border-radius: 999px; padding: 9px 16px; width: min(100%, 320px); }