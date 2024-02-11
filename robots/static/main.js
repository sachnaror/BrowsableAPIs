document.getElementById('manufacturerForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this);
    const jsonObject = {};

    for (const [key, value] of formData.entries()) {
        jsonObject[key] = value;
    }

    fetch('http://127.0.0.1:8000/manufacturer/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Add other headers here if needed, like Authorization for JWT tokens
        },
        body: JSON.stringify(jsonObject),
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log(data);
            alert('Manufacturer added successfully!');
            // Here you can redirect or clear the form as needed
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            alert('Error adding manufacturer.');
        });
});



























// const manufacturerId = document.getElementById('id').value;

// // Fetch Manufacturer Data
// window.onload = function () {
//     fetch(`http://127.0.0.1:8000/manufacturer/${id}`)
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById('name').value = data.name;
//         })
//         .catch(error => console.error('Error fetching data:', error));
// };

// // Update Manufacturer Data
// document.getElementById('updateBtn').addEventListener('click', function () {
//     const name = document.getElementById('name').value;

//     fetch(`http://127.0.0.1:8000/manufacturer/${manufacturerId}`, {
//         method: 'PUT',
//         headers: {
//             'Content-Type': 'application/json',
//             // Include additional headers as needed (e.g., Authorization)
//         },
//         body: JSON.stringify({ name: name }),
//     })
//         .then(response => {
//             if (response.ok) {
//                 alert('Manufacturer updated successfully!');
//             } else {
//                 alert('Error updating manufacturer.');
//             }
//         })
//         .catch(error => console.error('Error:', error));
// });

// // Delete Manufacturer
// document.getElementById('deleteBtn').addEventListener('click', function () {
//     if (confirm('Are you sure you want to delete this manufacturer?')) {
//         fetch(`http://127.0.0.1:8000/manufacturer/${manufacturerId}`, {
//             method: 'DELETE',
//             // Include additional headers as needed
//         })
//             .then(response => {
//                 if (response.ok) {
//                     alert('Manufacturer deleted successfully!');
//                     // Optionally redirect or clear form
//                 } else {
//                     alert('Error deleting manufacturer.');
//                 }
//             })
//             .catch(error => console.error('Error:', error));
//     }
// });
