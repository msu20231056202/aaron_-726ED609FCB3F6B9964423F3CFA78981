class Student {
  constructor(name, roll_number, cgpa) {
    this.name = name;
    this.roll_number = roll_number;
    this.cgpa = cgpa;
  }
}
function sort_students(student_list) {
  let sorted_students = student_list.sort((a, b) => b.cgpa - a.cgpa);
  return sorted_students;
}
// Example usage:
let student1 = new Student("Alice", "S123", 3.7);
let student2 = new Student("Bob", "S124", 3.9);
let student3 = new Student("Charlie", "S125", 3.5);
let student4 = new Student("David", "S126", 3.8);
let students = [student1, student2, student3, student4];
let sorted_students = sort_students(students);
// Print the sorted list of students by CGPA in descending order
sorted_students.forEach(student => {
  console.log(`Name: ${student.name}, Roll Number: ${student.roll_number}, CGPA: ${student.cgpa}`);
});