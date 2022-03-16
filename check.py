def get_passenger_name(self):
    return self.__passenger_name
def get_source(self):
    return self.__source
def get_destination(self):
    return self.__destination
def get_ticket_id(self):
    return self.__ticket_id

def validate_source_destination(self):
    if self._source== "delhi" and (self.destination=="mumbai" or self.destination=="chennai" or self.destination=="pune" or self._destination=="kolkata"):
        return True
    else:
        return False

def generate_ticket(self):
    if self.validate_source_destination() == True:
        srcchar=self.__source[0].upper()
        destchar=self.__destination[0].upper()
        if(Ticket.counter<10):
            self.__ticket_id=srcchar+destchar+"0"+str(Ticket.counter)
        else:
            self.__ticket_id=srcchar+destchar+str(Ticket.counter)
    else:
        self.__ticket_id=None
    return self.__ticket_id