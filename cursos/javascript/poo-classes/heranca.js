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

class ITBook extends Book {
  constructor(title, pages, isbn, technology) {
    super(title, pages, isbn);
    this.technology = technology;
  }
  printTechnology() {
    console.log(this.technology);
  }
}

let jsBook = new ITBook(
  'Learning JS Algorithms',
  '200',
  '1234567890',
  'Javascript'
);
console.log(jsBook.title);
console.log(jsBook.printTechnology());
