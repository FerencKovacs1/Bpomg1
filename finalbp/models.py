from django.db import models





class Hahuautok(models.Model):
    kep = models.ImageField(blank=True, null=True)


class Hahudeta(models.Model):
        rank = models.CharField(max_length=100)
        marka = models.CharField(max_length=100)
        kategoria = models.CharField(max_length=100)
        modell = models.CharField(max_length=100)
        tipus = models.CharField(max_length=100)
        uzemanyag = models.CharField(max_length=15)
        futottkm = models.CharField(max_length=10)
        evjarat = models.CharField(max_length=4)

        def __str__(self):
            return self.rank


class CachedImage(models.Model):
    url = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='HahuImg', blank=True, null=True)
    car = models.ForeignKey(Hahudeta, on_delete = models.CASCADE, related_name='images')

    def cache(self):
        """Store image locally if we have a URL"""

        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                    os.path.basename(self.url),
                    File(open(result[0], 'rb'))
                    )
            self.save()
