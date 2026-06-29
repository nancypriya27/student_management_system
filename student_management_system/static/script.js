function validateForm() {

    let marks = document.forms["studentForm"]["marks"].value;

    if (marks < 0 || marks > 100) {

        alert("Marks must be between 0 and 100");

        return false;
    }

    return true;
}

function confirmDelete() {

    return confirm("Are you sure you want to delete this student?");
}