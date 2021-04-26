class Book {
  constructor(title, pages, isbn) {
    this.title;
    this.pages;
    this.isbn;
  }
  printIsbn() {
    console.log(this.isbn);
  }
}

let book = new Book('title', 'pag', 'isbn');

console.log(book.title); // exibe o titulo do livro
book.title = 'new title'; //  atualiza o valor do titulo do livro
console.log(book.title); // exibe o titulo do livro
