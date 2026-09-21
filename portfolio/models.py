from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(max_length=120, default="Graphic Designer")
    availability = models.CharField(max_length=120, default="Available for freelance")
    hero_heading = models.CharField(max_length=180, default="Graphic design that speaks louder than words.")
    hero_text = models.TextField(default="Branding, posters, social media, and visual identity — crafted with bold ideas and pixel-perfect detail.")
    about_text = models.TextField(default="Hi, I'm Your Name — a graphic designer with a passion for bold, clean, and meaningful visuals. I help brands tell their story through design that stands out.")
    about_detail = models.TextField(default="With years of experience across branding, digital, and print, I turn ideas into visuals that connect.")
    about_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    skills = models.CharField(max_length=500, default="Adobe Photoshop, Illustrator, Figma, InDesign, After Effects, Branding")
    email = models.EmailField(default="hello@yourname.com")
    phone = models.CharField(max_length=50, default="+1 234 567 890")
    whatsapp = models.CharField(max_length=50, default="+1 987 654 321")
    office = models.CharField(max_length=50, blank=True, default="+1 122 334 455")
    tiktok_url = models.URLField("TikTok link", blank=True)
    facebook_url = models.URLField("Facebook link", blank=True)
    linkedin_url = models.URLField("LinkedIn link", blank=True)
    github_url = models.URLField("GitHub link", blank=True)
    instagram_url = models.URLField("Instagram link", blank=True)

    class Meta:
        verbose_name = "Portfolio profile"

    def __str__(self): return self.name

    @property
    def skills_list(self):
        return [skill.strip() for skill in self.skills.split(",") if skill.strip()]


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=80)
    image = models.ImageField(upload_to="projects/", null=True, help_text="Choose a project image from your computer")
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self): return self.title
