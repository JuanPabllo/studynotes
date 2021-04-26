interface Person {
  name: string;
  age: number;
}

function printName(person: Person) {
  console.log(person.name);
}

const john = { name: 'John', age: 21 };
const mary = { name: 'Mary', age: 21, phone: '123-456789' };

printName(john);
printName(mary);
