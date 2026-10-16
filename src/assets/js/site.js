(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('hauptmenue');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.querySelectorAll('.has-sub > a').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (window.matchMedia('(max-width: 900px)').matches && !a.parentNode.classList.contains('expanded')) {
        e.preventDefault();
        a.parentNode.classList.add('expanded');
      }
    });
  });
})();
