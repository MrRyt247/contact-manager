class ContactNode:
    def __init__(
        self,
        name: str,
        phone: str,
        other_phone: str = None,
        email: str = None,
        image_path: str = None,
    ):
        self.name = name
        self.phone = phone
        self.other_phone = other_phone
        self.email = email
        self.image_path = image_path
        self.is_favourite = False
        self.next = None


# Linked List implementation for contacts
class ContactList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_contact(
        self,
        name: str,
        phone: str,
        other_phone: str,
        email: str = "",
        image_path: str = None,
    ) -> None:
        new_contact = ContactNode(name, phone, other_phone, email, image_path)
        self.count += 1

        # If the list is empty, set the new contact as head
        if not self.head:
            self.head = new_contact
        else:
            # Insert alphabetically by name
            if self.head.name.lower() > name.lower():
                new_contact.next = self.head
                self.head = new_contact
            else:
                current = self.head
                # Find the correct position to insert
                while current.next and current.next.name.lower() <= name.lower():
                    current = current.next
                new_contact.next = current.next
                current.next = new_contact

    def delete_contact(self, name: str, phone: str) -> bool:
        if not self.head:
            return False

        # If head is the contact to delete
        if self.head.name == name and self.head.phone == phone:
            self.head = self.head.next
            self.count -= 1
            return True

        # Search for the contact
        current = self.head
        while current.next and not (
            current.next.name == name and current.next.phone == phone
        ):
            current = current.next

        # If contact found, delete it
        if current.next:
            current.next = current.next.next
            self.count -= 1
            return True
        return False

    def update_contact(
        self,
        old_name: str,
        old_phone: str,
        new_name: str,
        new_phone: str,
        new_other_phone: str,
        new_email: str = "",
        new_image_path: str = None,
    ) -> bool:
        # Delete the old contact
        if not self.delete_contact(old_name, old_phone):
            return False

        # Add the updated contact
        self.add_contact(
            new_name, new_phone, new_other_phone, new_email, new_image_path
        )
        return True

    def search_contacts(self, search_key: str) -> list:
        result = []
        current = self.head

        while current:
            # Check if search key is in name or phone number
            if (
                search_key.lower() in current.name.lower()
                or search_key in current.phone
            ):
                result.append(
                    {
                        "name": current.name,
                        "phone": current.phone,
                        "email": current.email,
                        "image_path": current.image_path,
                    }
                )
            current = current.next
        return result

    def get_all_contacts(self) -> list:
        result = []
        current = self.head

        while current:
            result.append(
                {
                    "name": current.name,
                    "phone": current.phone,
                    "email": current.email,
                    "image_path": current.image_path,
                }
            )
            current = current.next
        return result
