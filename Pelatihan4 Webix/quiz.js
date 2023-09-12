// nge parse nama masukin ke table
const small_film_set = [
  { nama: 'Budi', hobby: 'Badminton', gol: 'O', pekerjaan: 'Mahasiswa' },
  { nama: 'Andi', hobby: 'Sepak Bola', gol: 'A', pekerjaan: 'Mahasiswa' },
  { nama: 'Caca', hobby: 'Basket', gol: 'B', pekerjaan: 'Mahasiswa' },
  { nama: 'Dedi', hobby: 'Renang', gol: 'AB', pekerjaan: 'Mahasiswa' },
];

webix.ui({
  view: 'form',
  id: 'form1',
  scroll: false,
  //width: 300,
  elements: [
    { view: 'text', label: 'Nik', name: 'email' },
    {
      view: 'text',
      label: 'Nama',
      name: 'nama',
      id: 'name',
      on: {
        onTimedKeyPress: function () {
          var value = this.getValue().toLowerCase();

          $$('tableData').filter(function (obj) {
            return obj.nama.toLowerCase().indexOf(value) !== -1;
          });
        },
      },
    },
    {
      view: 'datatable',
      id: 'tableData',
      columns: [
        { id: 'nama', editor: 'text', header: 'Nama', width: 50 },
        { id: 'hobby', editor: 'text', header: 'Hobby', width: 200 },
        { id: 'gol', editor: 'text', header: 'Golongan Darah', width: 80 },
        { id: 'pekerjaan', editor: 'text', header: 'Pekerjaan', width: 100 },
      ],
      editable: true,
      data: small_film_set,
    },
  ],
});
