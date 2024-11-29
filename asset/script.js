// Fetch the JSON file
fetch('data/books.json')
    .then(response => response.json()) // Parse the JSON
    .then(data => {
        const bookList = document.getElementById('book-list');
        data.forEach(book => {
            // Create a container for each book
            const bookDiv = document.createElement('div');
            bookDiv.className = 'book';

            // Add the book image
            const img = document.createElement('img');
            img.src = book.image;
            img.alt = book.name;
            bookDiv.appendChild(img);

            // Add the book name
            const title = document.createElement('h3');
            title.textContent = book.name;
            bookDiv.appendChild(title);

            // Add the link
            const link = document.createElement('a');
            link.href = book.link;
            link.textContent = 'View Book';
            link.target = '_blank'; // Open in a new tab
            bookDiv.appendChild(link);

            // Append the bookDiv to the book list
            bookList.appendChild(bookDiv);
        });
    })
    .catch(error => console.error('Error fetching books:', error));
