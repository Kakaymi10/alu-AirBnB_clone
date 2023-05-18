# AIRBNB CLONE: THE CONSOLE

This is an Airbnb clone project that aims to replicate some functionalities of the Airbnb platform. The project includes a command-line interface (CLI) called "The Console" which allows users to interact with the application and perform various operations.

## Command Interpreter

The command interpreter, also known as "The Console," is a command-line interface that provides a way to interact with the Airbnb clone application. It allows users to manage and manipulate objects within the application, such as creating, updating, and deleting objects, as well as performing various operations and queries.

### How to Start

To start the command interpreter, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the project directory where the Airbnb clone code is located.
3. Run the following command to start the console:

   ```
   $ ./console.py
   ```

   or

   ```
   $ python console.py
   ```

4. The command interpreter will start, and you will see a prompt indicating that it's ready to accept commands.

### How to Use

Once the command interpreter is running, you can enter various commands to interact with the application. The commands follow a specific syntax:

```
command_name [arguments] [options]
```

Here's an overview of the available commands and their usage:

- **`create`**: Create a new object.
  ```
  (hbnb) create <class_name>
  ```

- **`show`**: Display information about a specific object.
  ```
  (hbnb) show <class_name> <object_id>
  ```

- **`update`**: Update the attributes of an object.
  ```
  (hbnb) update <class_name> <object_id> <attribute_name> "<attribute_value>"
  ```

- **`destroy`**: Delete an object.
  ```
  (hbnb) destroy <class_name> <object_id>
  ```

- **`all`**: Show all objects or objects of a specific class.
  ```
  (hbnb) all
  (hbnb) all <class_name>
  ```

- **`quit`**: Exit the console.
  ```
  (hbnb) quit
  ```

### Examples

Here are some examples of how to use the command interpreter:

- Create a new user object:
  ```
  (hbnb) create User
  ```

- Show information about a specific place object:
  ```
  (hbnb) show Place 123456
  ```

- Update the name attribute of an existing review object:
  ```
  (hbnb) update Review 7890 name "New Review Name"
  ```

- Delete a specific object:
  ```
  (hbnb) destroy City 9876
  ```

- Show all objects of a specific class:
  ```
  (hbnb) all State
  ```

- Quit the console:
  ```
  (hbnb) quit
  ```

Feel free to explore and use the command interpreter to interact with the Airbnb clone application, create objects, retrieve information, perform updates, and more.

Enjoy using Airbnb Clone: The Console!
