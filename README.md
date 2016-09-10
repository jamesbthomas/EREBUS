#EREBUS
##A Local Password Vault

### Background / Features
EREBUS is a local password vault application with a number of features. It's primary
feature is to encrypt a user-input passphrase based on the user's choice of encryption method.
For example, if a user wants to use "tyranosauras" as their password for a bank or email account,
most services will recognize that the password is too weak. EREBUS will take that password, allow
the user to select an encryption method from a number of options, such as a ceasar cipher, and return
an encrypted version of that passphrase that will, most likely, be a more secure password than the original.
Additionally, EREBUS will also function as a password vault, saving identifiers and passwords for a users accounts
on their local machine. Given a user's password or passphrase and an identifier, EREBUS will save that combination
to a hidden, encrypted file, accessible only by the EREBUS executable. EREBUS will also have functionality to
return a password given that password's identifier. In order to ensure the security of this app, EREBUS will also prompt
the user for a single password whenever the application opens.

###**DISCLAIMER**
This is an amateur project. It's features may prove useful, either as a functioning password vault or for instructional purposes,
but is in no way meant to effectively protect your information. This project will strive to achieve that level of sophistication and security,
but users are advised against storing important or sensitive information within the EREBUS vault.

### Implemented Features
- README updated with initial project description

### TODO List
- Create dev branches
- 

### Branch Allocations
- master: this branch will be home to the most recent, working source code in python
- dev: this is the main development branch that other feature branches will come from
- cdev: this is the main branch for work in c. cdev and dev will work independently from one another, with cdev eventually trying to 
be an exact copy of the dev branch

###LICENSE
Copyright CDT James Thomas, Project Manager, and CDT Zachary Royal, Collaborator, USMA 2017. Free for instructional and/or personal use.
Contact james.b.thomas@mac.com for commercial/business requests.
