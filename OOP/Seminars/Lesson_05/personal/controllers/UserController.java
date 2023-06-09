package Lesson_05.personal.controllers;

import Lesson_05.personal.model.Repository;
import Lesson_05.personal.model.User;
import Lesson_05.personal.views.Validation;

import java.util.List;

public class UserController {
    private final Repository repository;
    private final Validation validator;

    public UserController(Repository repository, Validation validator) {
        this.repository = repository;
        this.validator = validator;
    }

    public void saveUser(User user) throws Exception {
        validator.validateUser(user);
        repository.CreateUser(user);
    }

    public User readUser(String userId) throws Exception {
        List<User> users = repository.getAllUsers();
        User user = userSearch(userId, users);
        return user;
        }

    private static User userSearch(String userId, List<User> users) throws Exception {
        for (User user : users) {
            if (user.getId().equals(userId)) {
                return user;
            }
        }
        throw new Exception("User not found");
    }

    public void userUpdate(String userId, User newUser) throws Exception{
        validator.validateUser(newUser);
        List<User> users = repository.getAllUsers();
        User user = userSearch(userId, users);
        user.setFirstName(newUser.getFirstName()); 
        user.setLastName(newUser.getLastName());
        user.setPhone(newUser.getPhone());
        repository.saveUser(users);
    }

    public List<User> readAllUsers() {
        return repository.getAllUsers();
    }

    public void updateUser() {

    }
}