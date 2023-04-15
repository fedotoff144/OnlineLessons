package Lesson_05.personal.views;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import Lesson_05.personal.model.User;

public class Validation {
    Pattern namePattern = Pattern.compile("^\\S+$");
    Pattern phonePattern = Pattern.compile("^\\d+$");
    public void validateUser(User inputUser) throws Exception{
        Matcher nameMatcher = namePattern.matcher(inputUser.getFirstName());
        Matcher lastnameMatcher = namePattern.matcher(inputUser.getLastName());
        Matcher phoneMatcher = phonePattern.matcher(inputUser.getPhone());

        if(!nameMatcher.find(0)){
            throw new Exception("Такое имя недопустимо!");
        }
        if(!lastnameMatcher.find(0)){
            throw new Exception("Такая фамилия недопустима!");
        }
        if(!phoneMatcher.find(0)){
            throw new Exception("Такой номер телефона недопустим!");
        }
    }
}
