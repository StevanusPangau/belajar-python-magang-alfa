let form1 = [
  { view: 'text', label: 'Email', name: 'email', required: true },
  {
    view: 'text',
    label: 'Coba',
    name: 'coba',
    id: 'coba',
    required: true,
    on: {
      onChange: function (newValue, oldValue) {
        let form = this.getFormView();
        let valueEmail = form.elements.email.getValue();
        webix.message(`email : ${valueEmail}`);
        webix.message(`old value : ${oldValue} | new value : ${newValue}`);
      },
    },
  },
  { view: 'text', type: 'password', label: 'Password', name: 'password', required: true, labelWidth: 'auto' },
  {
    cols: [
      {
        view: 'button',
        id: 'btnLogin',
        value: 'Login',
        css: 'webix_primary',
        click: function () {
          if ($$('form1').validate()) webix.message('Berhasil Login');
          else webix.message({ type: 'error', text: 'Form data is invalid' });
        },
      },
      {
        view: 'button',
        value: 'Cancel',
        id: 'btnCancel',
        css: 'webix_danger',
        on: {
          onItemClick: function () {
            // console.log(this.getFormView().elements);
            console.log($$('form1').elements);
            $$('form1').parse({ email: '', coba: '', password: '' });
            webix.message('Tekan Tombol Cancel');
          },
        },
      },
      {
        view: 'button',
        value: 'Add Data',
        id: 'btnDummy',
        on: {
          onItemClick: function () {
            $$('form1').parse({ email: 'Evan@gmail.com', coba: 'Coba', password: '123' });
            webix.message('Data Sudah Ditambahkan');
          },
        },
      },
    ],
  },
];

webix.ui({
  view: 'form',
  id: 'form1',
  scroll: false,
  //width: 300,
  elements: form1,
  rules: {
    // untuk validasi
    email: webix.rules.isEmail,
    password: webix.rules.isNotEmpty,
    coba: webix.rules.isNotEmpty,
  },
});

$$('form1').elements['email'].attachEvent('onChange', function (newv, oldv, config) {
  webix.message(`Value was changed from ${oldv} to ${newv}. Source: ${config}`);
});

// $$('form1').elements['password'].attachEvent('onChange', function (newv, oldv, config) {
//   webix.message(`Value was changed from ${oldv} to ${newv}. Source: ${config}`);
// });
