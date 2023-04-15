package Lesson_05.personal;

import Lesson_05.personal.controllers.UserController;
import Lesson_05.personal.model.FileOperation;
import Lesson_05.personal.model.FileOperationImpl;
import Lesson_05.personal.model.Repository;
import Lesson_05.personal.model.RepositoryFile;
import Lesson_05.personal.views.Validation;
import Lesson_05.personal.views.ViewUser;

public class Main {
    public static void main(String[] args) {
        FileOperation fileOperation = new FileOperationImpl("users.txt");
        Repository repository = new RepositoryFile(fileOperation);
        UserController controller = new UserController(repository, new Validation());
        ViewUser view = new ViewUser(controller);
        view.run();
    }
}