fetch('http://localhost:5000/api/v1/dialogs')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            dialogs = myjson.dialogs;
            console.dir(dialogs[0].users)
            document.getElementById("my_id").src = "data:image/png;base64," + dialogs[0].users[0].avatar;
        });
