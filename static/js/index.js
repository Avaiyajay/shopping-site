let updateCartBtns = document.getElementsByClassName('update-cart')

for(let i = 0;i<updateCartBtns.length;i++)
{
    updateCartBtns[i].addEventListener('click',function(){
           let productid = this.dataset.productid
           let action = this.dataset.action
           if(user === 'AnonymousUser')
           {
                setcookie(productid,action);
           }
           else{
                updatecart(productid,action)
           }
    })
}

function readCookie(name)
{
       var ca = document.cookie.split(';');
       var nameEQ = name + "=";
       for(var i=0; i < ca.length; i++) {
              var c = ca[i];
              while (c.charAt(0)==' ') c = c.substring(1, c.length); //delete spaces
              if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
       }
       return null;
}

cart = JSON.parse(readCookie('cart'));

if(cart == undefined)
{
       cart = {};
       document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/"
       location.reload();
}
function setcookie(productid,action)
{
       
       if(action == 'add')
       {
              if(cart[productid] == undefined)
              {
                     cart[productid] = {
                            'quantity' : 1
                     }
              }
              else{
                     cart[productid]['quantity'] += 1
              }
              
       }

       if(action == 'remove')
       {
              cart[productid]['quantity'] -= 1
       }

       if(cart[productid]['quantity'] <=0 )
       {
              delete cart[productid]
       }

       document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/"
       console.log("cookie is created ");
       location.reload();
}

function updatecart(productid,action)
{
       console.log("inside updatecart function")
       let url = 'updatecart'
       fetch(url,{
              method : 'POST',
              headers : {
                    'Content-Type':'application/json',
                    'X-CSRFToken' : csrftoken
              },
              body : JSON.stringify({'productid':productid,'action':action})
       })
       .then( (response) => {
            return response.json()
       })
       .then( (data) => {
              location.reload();
       })
}