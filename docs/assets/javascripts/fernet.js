const clipboardIcon = '<svg style="width:16px;height:16px" viewBox="0 0 24 24"><path fill="currentColor" d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3" /></svg>';

const clipboardCheckIcon = '<svg style="width:16px;height:16px" viewBox="0 0 24 24"><path fill="currentColor" d="M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3Z" /></svg>';

window.addEventListener('DOMContentLoaded', (event) => {
  const fernetKeyGenerators = document.getElementsByClassName('fernet-key-generator');
  for (let i = 0; i < fernetKeyGenerators.length; i++) {
    const fernetKeyGenerator = fernetKeyGenerators.item(i);

    const outputBox = document.createElement('div');
    outputBox.className = 'output-box';

    const output = document.createElement('input');
    output.className = 'md-input';
    output.disabled = true;

    const copyButton = document.createElement('button');
    copyButton.type = "button"
    copyButton.className = "clipboard-button md-clipboard md-icon";
    copyButton.disabled = true;

    outputBox.appendChild(output);
    outputBox.appendChild(copyButton);

    const button = document.createElement('button');
    button.type = "button";
    button.className = 'md-button';
    button.innerText = 'Generate key';

    fernetKeyGenerator.appendChild(outputBox);
    fernetKeyGenerator.appendChild(button);

    let key = '';
    button.addEventListener('click', () => {
      button.disabled = true;
      fetch('https://fernet-key-generator.deta.dev').then((response) => {
        response.text().then((newKey) => {
          key = newKey;
          button.disabled = false;
          copyButton.disabled = false;
          output.value = key;
        });
      });
    });

    copyButton.addEventListener('click', () => {
      navigator.clipboard.writeText(key);
    });
  }
});
