import factory


class OrganizationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'organizations.Organization'

    name = "Combined Charity"
    description = "This is a great charity"
    website = "www.google.com"
    org_type = "Charity"
