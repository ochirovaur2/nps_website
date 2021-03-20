function onSubmit(token) {
  console.log(token)
 
  
    
    let textarea = $('.rating-form__textarea');
    
    
   
      let length_of_text = textarea.val().length
      console.log(length_of_text)
      let rating = $("input:radio[name=rating]:checked").val();

      if (rating == null) {
        
        textarea.attr("placeholder", "Пожалуйста, поставьте оценку");
        // $('.rating-form__label').html("Пожалуйста, поставьте оценку");
        textarea.css('border', '2px solid #EC432E'); 

      } else if (rating < 3 && length_of_text < 3){

        
        textarea.attr("placeholder", "Пожалуйста, напишите комментарий не менее трех символов");
        $('.rating-form__label').html("Пожалуйста, напишите комментарий не менее трех символов");
        textarea.css('border', '2px solid #EC432E'); 

      } else{
        document.getElementById("rating-form-js").submit();
      }

    

    textarea.on('input', function(){
      textarea.css('border', '1px solid #55C57A');
      textarea.css('border', '1px solid black');
      textarea.css('border-bottom', '3px solid #55C57A ');
    });  
  

  
};