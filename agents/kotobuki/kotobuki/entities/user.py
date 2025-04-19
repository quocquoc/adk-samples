# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""User entity module for Kotobuki agent."""

from typing import List, Dict, Optional
from pydantic import BaseModel, Field, ConfigDict


class Contact(BaseModel):
    """Represents a contact person."""

    name: str
    relationship: str
    phone_number: str
    model_config = ConfigDict(from_attributes=True)


class MedicalInfo(BaseModel):
    """Placeholder for basic medical information."""

    primary_doctor_name: Optional[str] = None
    primary_doctor_phone: Optional[str] = None
    known_allergies: List[str] = Field(default_factory=list)
    regular_medications: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    """Represents an elderly user of the Kotobuki agent."""

    user_id: str
    first_name: str
    last_name: str
    phone_number: str
    address: Optional[str] = None # Simplified address
    emergency_contacts: List[Contact] = Field(default_factory=list)
    caregiver_contacts: List[Contact] = Field(default_factory=list)
    relative_contacts: List[Contact] = Field(default_factory=list)
    medical_info: MedicalInfo = Field(default_factory=MedicalInfo)
    interests: List[str] = Field(default_factory=list)
    # Add other relevant fields as needed, e.g., preferred language, mobility status
    model_config = ConfigDict(from_attributes=True)

    def to_json(self) -> str:
        """
        Converts the User object to a JSON string.

        Returns:
            A JSON string representing the User object.
        """
        return self.model_dump_json(indent=4)

    @staticmethod
    def get_user(current_user_id: str) -> Optional["User"]:
        """
        Retrieves a user based on their ID.

        Args:
            current_user_id: The ID of the user to retrieve.

        Returns:
            The User object if found, None otherwise.
        """
        # In a real application, this would involve a database lookup.
        # For this example, we'll return a dummy user.
        # You should replace this with actual user data loading.
        if current_user_id == "user001":
            return User(
                user_id=current_user_id,
                first_name="Haru",
                last_name="Tanaka",
                phone_number="+81-3-5555-1234", # Example Japanese number
                address="1-1 Chiyoda, Chiyoda City, Tokyo",
                emergency_contacts=[
                    Contact(name="Emergency Services", relationship="Emergency", phone_number="119") # Japan emergency number
                ],
                caregiver_contacts=[
                    Contact(name="Aiko Sato", relationship="Caregiver", phone_number="+81-90-1111-2222")
                ],
                relative_contacts=[
                    Contact(name="Kenji Tanaka", relationship="Son", phone_number="+81-80-3333-4444"),
                    Contact(name="Yumi Tanaka", relationship="Granddaughter", phone_number="+81-70-5555-6666")
                ],
                medical_info=MedicalInfo(
                    primary_doctor_name="Dr. Yamamoto",
                    primary_doctor_phone="+81-3-6666-7777",
                    known_allergies=["Pollen"],
                    regular_medications=["Blood pressure medication"]
                ),
                interests=["Gardening", "Reading", "Listening to classical music", "Talking about grandchildren"],
            )
        else:
             # Default or fallback user if ID doesn't match
            return User(
                user_id=current_user_id,
                first_name="Default",
                last_name="User",
                phone_number="+1-000-000-0000",
                emergency_contacts=[Contact(name="Emergency Services", relationship="Emergency", phone_number="911")]
            )
