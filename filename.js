const fs = require('fs');

function listFilesInFolder(folderPath) {
    fs.readdir(folderPath, (err, files) => {
        if (err) {
            console.error('Error reading folder:', err);
            return;
        }
        files.forEach(file => {
            console.log(file);
        });
    });
}

const folderPath = 'static/images';
listFilesInFolder(folderPath);
