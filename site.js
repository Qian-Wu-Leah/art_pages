(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('[data-lightbox]'));
  if (!links.length) return;

  var box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.innerHTML =
    '<button class="close" aria-label="Close">&times;</button>' +
    '<button class="prev" aria-label="Previous">&#8249;</button>' +
    '<img alt="">' +
    '<button class="next" aria-label="Next">&#8250;</button>';
  document.body.appendChild(box);

  var img = box.querySelector('img');
  var index = 0;

  function show(i) {
    index = (i + links.length) % links.length;
    img.src = links[index].getAttribute('href');
    img.alt = links[index].querySelector('img').alt || '';
  }
  function open(i) { show(i); box.classList.add('open'); }
  function close() { box.classList.remove('open'); img.removeAttribute('src'); }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); open(i); });
  });

  box.querySelector('.close').addEventListener('click', close);
  box.querySelector('.prev').addEventListener('click', function () { show(index - 1); });
  box.querySelector('.next').addEventListener('click', function () { show(index + 1); });
  box.addEventListener('click', function (e) { if (e.target === box) close(); });

  document.addEventListener('keydown', function (e) {
    if (!box.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(index - 1);
    if (e.key === 'ArrowRight') show(index + 1);
  });
})();

(function () {
  var form = document.querySelector('form.contact');
  if (!form) return;
  var status = form.querySelector('.form-status');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.textContent = 'Sending...';
    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    }).then(function (r) {
      if (r.ok) {
        form.reset();
        status.textContent = 'Success! Message received.';
      } else {
        status.textContent = 'Something went wrong. Please email me directly.';
      }
    }).catch(function () {
      status.textContent = 'Something went wrong. Please email me directly.';
    });
  });
})();
