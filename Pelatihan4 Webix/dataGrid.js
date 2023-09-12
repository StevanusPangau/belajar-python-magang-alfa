webix.ui({
  view: 'datatable',
  id: 'sample-datagrid',
  columns: [
    { id: 'rank', editor: 'text', header: '', width: 50 },
    { id: 'title', editor: 'text', header: 'Film title', width: 200 },
    { id: 'year', editor: 'text', header: 'Released', width: 80 },
    { id: 'votes', editor: 'text', header: 'Votes', width: 100 },
  ],
  editable: true,
  data: [
    { id: 1, title: 'The Shawshank Redemption', year: 1994, votes: 678790, rank: 1 },
    { id: 2, title: 'The Godfather', year: 1972, votes: 511495, rank: 2 },
  ],
});

console.log($$('sample-datagrid').config.columns);
