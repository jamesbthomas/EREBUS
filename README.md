#EREBUS
##A local password vault

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

### Implemented Features
- README updated with initial project description

### TODO List
- Determine languages to use (c/scala/python)
- Create dev branches

### Branch Allocations
- master: this branch will be home to the most recent, working executable and only the executable.
- src: this branch will be home to the source code for the most-recent working executable located on master. the executable may be stored here as well
- mainDev: this is the main development branch that other feature branches will come from

###LICENSE
Copyright CDT James Thomas, Project Manager, and CDT Zachary Royal, Collaborator, USMA. Free for instructional and/or personal use.
Contact james.b.thomas@mac.com for commercial/business requests.
