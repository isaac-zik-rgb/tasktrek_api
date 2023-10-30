const formEl = document.querySelector('.registration_form');
const submitForm =  async (event) => {
    event.preventDefault();

    try {
        const formData = new FormData(formEl);
        const errorMesg = document.getElementById('message');
    
        const data = Object.fromEntries(formData);
        const password = data.password;
        const confirmPass = data.comfirm_password; // Corrected the field name
    
        if (password !== confirmPass) {
            errorMesg.textContent = 'Sorry, your passwords do not match';
            setTimeout(() => {
                errorMesg.textContent = '';
            }, 1000);
        }
        const res = await fetch('http://127.0.0.1:8000/api/account/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (!res.ok){
            const response = await res.json();

            console.log(response);
            return;
        }
        const response = await res.json();
        console.log(response)

        window.location.href = '/login.html'
        

    } catch (error) {
        console.log(error);
    }

   
};

formEl.addEventListener('submit', submitForm)