const form = document.querySelector('form');
console.log("form element", form)
form.addEventListener('submit', (e) => {
  e.preventDefault(); // Prevent page reload
  
  const data = new FormData(e.target);
  const values = Object.fromEntries(data.entries());
  alert(values)
  console.log(values);
});
