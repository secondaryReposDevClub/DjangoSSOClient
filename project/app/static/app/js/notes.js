const createBtn = document.getElementById('createBtn');
const form = document.getElementById('noteForm');

createBtn.addEventListener('click', () => {
    form.classList.toggle('active');
});
