window.addEventListener('DOMContentLoaded', (event) => {
  window.document$.subscribe(() => {
    const fernetKeyGenerators = document.getElementsByClassName('fernet-key-generator');
    for (let i = 0; i < fernetKeyGenerators.length; i++) {
      const fernetKeyGenerator = fernetKeyGenerators.item(i);

      const output = fernetKeyGenerator.getElementsByTagName('code').item(0);
      const button = fernetKeyGenerator.getElementsByClassName('md-button').item(0);

      button.addEventListener('click', () => {
        button.disabled = true;
        fetch('https://fernet-key-generator.deta.dev').then((response) => {
          response.text().then((key) => {
            button.disabled = false;
            output.innerText = key;
          });
        });
      });
    }
  });
});
