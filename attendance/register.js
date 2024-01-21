// ... (other code)

// Function to handle form submission
function registerMember() {
    // Get form values
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var phone = document.getElementById("phone").value;
    var residence = document.getElementById("residence").value;
    var department = document.getElementById("department").value; // Add this line
    var fellowship = document.getElementById("fellowship").value; // Add this line
    var faceId = "some_generated_face_id"; // You need to generate this

    // Create data object
    var data = {
        name: name,
        age: age,
        phone: phone,
        residence: residence,
        department: department, // Add this line
        fellowship: fellowship, // Add this line
        face_id: faceId
    };

    // Send POST request to register_member route
    fetch("/register_member", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);
        // Reset form fields
        document.getElementById("name").value = "";
        document.getElementById("age").value = "";
        document.getElementById("phone").value = "";
        document.getElementById("residence").value = "";
        document.getElementById("department").value = ""; // Add this line
        document.getElementById("fellowship").value = ""; // Add this line
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

// ... (other code)




