function get_data() {
    let query_member = document.getElementById("query_member").value;
    let msg = document.getElementById("query_result");
    let url = `http://127.0.0.1:3000/api/members?username=${query_member}`;
    let name = null;

    fetch(url)
    .then(function(response){
        return response.json();
    })
    .then(function(my_json){
        if (my_json.data == null){
            msg.textContent = "查詢不到該會員";
        } else {
            name = my_json.data.name;
            msg.textContent = `${name}(${query_member})` ;
        }    
    })
} 

function update_name(){
    let revise_name = document.getElementById("revise_name").value;
    let update_msg = document.getElementById("update_result");
    let url = "http://127.0.0.1:3000/api/member";
    let data = {"name":revise_name}
    
    fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: new Headers({
            "Content-Type": "application/json"
        })
    }).then(function(response){
        return response.json();
    }).then(function(res_json){
        if (res_json.ok){
            update_msg.textContent = "更新成功";
        } else if (res_json.error){
            update_msg.textContent = "更新失敗";
        }
    });
}