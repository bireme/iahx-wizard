from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils.translation import ugettext_lazy as _, get_language
from django.template.defaultfilters import slugify

LANGUAGES_CHOICES = (
    ('en', _('English')), # default language
    ('pt-BR', _('Portuguese')),
    ('es', _('Spanish')),
)


class Generic(models.Model):
    class Meta:
        abstract = True

    created_time = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    updated_time = models.DateTimeField(_("updated"), auto_now=True, editable=False, null=True, blank=True)
    created_by = CurrentUserField(related_name="+", editable=False)
    updated_by = CurrentUserField(on_update=True, related_name="+", editable=False)


class Wizard(Generic):
    class Meta:
        verbose_name = _("Wizard")
        verbose_name_plural = _("Wizards")

    name = models.CharField(_('Name'), max_length=125, blank=False)
    code = models.SlugField(_('Code'), max_length=125, default='', editable=False)

    def save(self, *args, **kwargs):
        self.code = slugify(self.name)
        super(Wizard, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Step(Generic):
    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")

    wizard = models.ForeignKey(Wizard, verbose_name=_("Wizard"), blank=False, on_delete=models.PROTECT)
    step_number = models.SmallIntegerField(_("Step"), null=True, default=1)
    language = models.CharField(_("Language"), max_length=10, choices=LANGUAGES_CHOICES)
    label = models.CharField(_("Label"), max_length=255)
    filter_name = models.CharField(_("Filter name"), blank=True, max_length=55)

    def __str__(self):
        return '{} | {} | {}'.format(self.wizard, self.step_number, self.label)

class StepLocal(models.Model):

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    step = models.ForeignKey(Step, verbose_name=_("Step"), on_delete=models.CASCADE)
    language = models.CharField(_("Language"), max_length=10, choices=LANGUAGES_CHOICES)
    label = models.CharField(_("Label"), max_length=255)

    def __str__(self):
        return self.label


class Option(Generic):

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    step = models.ForeignKey(Step, verbose_name=_("Step"), blank=False, on_delete=models.PROTECT)
    language = models.CharField(_("Language"), max_length=10, choices=LANGUAGES_CHOICES)
    label = models.CharField(_('Option'), max_length=255)
    group = models.SmallIntegerField(_("Group"), null=True, blank=True)
    filter_query = models.CharField(_('Filter query'), max_length=125, blank=True)

    def __str__(self):
        lang_code = get_language()
        translation = OptionLocal.objects.filter(option_id=self.id, language=lang_code)
        label = self.label
        if translation:
            label = translation[0].label

        return label

class OptionLocal(models.Model):

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")

    option = models.ForeignKey(Option, verbose_name=_("Option"), on_delete=models.CASCADE)
    language = models.CharField(_("Language"), max_length=10, choices=LANGUAGES_CHOICES)
    label = models.CharField(_("Label"), max_length=255)

    def __str__(self):
        return self.label
