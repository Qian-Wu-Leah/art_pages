(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('[data-lightbox]'));
  if (!links.length) return;

  var box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'Artwork details');
  box.innerHTML =
    '<div class="lightbox-controls">' +
      '<button class="expand" aria-label="Enlarge image" aria-pressed="false">&#8599;</button>' +
      '<button class="close" aria-label="Close">&times;</button>' +
    '</div>' +
    '<div class="lightbox-content">' +
      '<button class="prev" aria-label="Previous image">&#8249;</button>' +
      '<div class="lightbox-media"><img alt=""></div>' +
      '<button class="next" aria-label="Next image">&#8250;</button>' +
      '<aside class="lightbox-info">' +
        '<h2></h2>' +
        '<p class="lightbox-year"></p>' +
        '<p class="lightbox-medium"></p>' +
      '</aside>' +
    '</div>';
  document.body.appendChild(box);

  var img = box.querySelector('img');
  var title = box.querySelector('.lightbox-info h2');
  var year = box.querySelector('.lightbox-year');
  var medium = box.querySelector('.lightbox-medium');
  var expandButton = box.querySelector('.expand');
  var index = 0;

  function show(i) {
    index = (i + links.length) % links.length;
    var link = links[index];
    var thumbnail = link.querySelector('img');
    var filename = link.getAttribute('href').split('/').pop().replace(/\.[^.]+$/, '');
    title.textContent = link.dataset.title || thumbnail.alt || filename;
    year.textContent = link.dataset.year || 'Not listed';
    medium.textContent = link.dataset.medium || '';
    medium.hidden = !link.dataset.medium;
    img.src = link.getAttribute('href');
    img.alt = title.textContent;
  }
  function open(i) { show(i); box.classList.add('open'); }
  function close() {
    box.classList.remove('open', 'expanded');
    expandButton.setAttribute('aria-pressed', 'false');
    expandButton.setAttribute('aria-label', 'Enlarge image');
    img.removeAttribute('src');
  }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); open(i); });
  });

  expandButton.addEventListener('click', function () {
    var expanded = box.classList.toggle('expanded');
    expandButton.setAttribute('aria-pressed', String(expanded));
    expandButton.setAttribute('aria-label', expanded ? 'Show details' : 'Enlarge image');
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
