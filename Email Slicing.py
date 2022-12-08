while(True):
    email_id=input("Enter email id: ")
    username=email_id[:email_id.index('@')]
    domain=email_id[email_id.index('@')+1:]
    a=domain.upper()
    print(f"username:{username} and domain:{(a)}")

