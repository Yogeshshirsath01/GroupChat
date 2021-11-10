document.addEventListener('DOMContentLoaded', function () {
    let pathname = document.location.pathname
    let addbutton = document.querySelector('#addbutton')
    let edit = document.querySelector('#edit')  
    
    addbutton.addEventListener('click', function () {
        if (document.querySelector('#addform').classList.contains("d-none")) {
            document.querySelector('#addform').classList.remove("d-none");
            document.body.style.backgroundColor = "white";
        } else {
            document.querySelector('#addform').classList.add("d-none");
            document.body.style.backgroundColor = "#ededed";
        }
    })
    let headline = document.querySelector('#headline');
    edit.addEventListener('click', function () {
            edit.style.display = 'none'
            headline.innerHTML =
                ` <form id="edit-post-form" class="card-text row" style="margin-top: 23px;">
                    <div class="form-group" >
                        <textarea 
                            style="overflow: hidden; height:45px;font-weight: bold;font-size: 20px;"
                            class="form-control"
                            id="edit-post-textarea">${headline.innerHTML}</textarea>
                    </div>
                    <input type="submit" style="height:45px;" class="btn btn-primary post-submit" value="Save"/>
                </form>`
        document.querySelector('#edit-post-form').onsubmit = () => {
            const content = document.querySelector('#edit-post-textarea').value;
            let editbutton = document.querySelector('#content').value;
            console.log(editbutton);

            fetch('/postedit', {
                method: 'PUT',
                body: JSON.stringify({content, editbutton})
            })
                .then(response => response.json())
                .then(result => {
                    if (result.error) {
                        console.log(`Error editing post: ${result.error}`);
                    };
                })  
        }

        
    });

    // edit.addEventListener('click', function () {
    //     console.log('edit');
    // });
})

