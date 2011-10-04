from warnings import warn
import ufoLib
from defcon.objects.base import BaseObject


class Info(BaseObject):

    """
    This object represents info values.

    **This object posts the following notifications:**

    ============  ====
    Name          Note
    ============  ====
    Info.Changed  Posted when the *dirty* attribute is set.
    ============  ====

    **Note:** The documentation strings here were automatically generated
    from the `UFO specification <http://unifiedfontobject.org/filestructure/fontinfo.html>`_.
    """

    changeNotificationName = "Info.Changed"
    beginUndoNotificationName = "Info.BeginUndo"
    endUndoNotificationName = "Info.EndUndo"
    beginRedoNotificationName = "Info.BeginRedo"
    endRedoNotificationName = "Info.EndRedo"

    def __init__(self):
        super(Info, self).__init__()
        self._ascender = None
        self._capHeight = None
        self._copyright = None
        self._descender = None
        self._familyName = None
        self._italicAngle = None
        self._macintoshFONDFamilyID = None
        self._macintoshFONDName = None
        self._note = None
        self._openTypeHeadCreated = None
        self._openTypeHeadFlags = None
        self._openTypeHeadLowestRecPPEM = None
        self._openTypeHheaAscender = None
        self._openTypeHheaCaretOffset = None
        self._openTypeHheaCaretSlopeRise = None
        self._openTypeHheaCaretSlopeRun = None
        self._openTypeHheaDescender = None
        self._openTypeHheaLineGap = None
        self._openTypeNameCompatibleFullName = None
        self._openTypeNameDescription = None
        self._openTypeNameDesigner = None
        self._openTypeNameDesignerURL = None
        self._openTypeNameLicense = None
        self._openTypeNameLicenseURL = None
        self._openTypeNameManufacturer = None
        self._openTypeNameManufacturerURL = None
        self._openTypeNamePreferredFamilyName = None
        self._openTypeNamePreferredSubfamilyName = None
        self._openTypeNameSampleText = None
        self._openTypeNameUniqueID = None
        self._openTypeNameVersion = None
        self._openTypeNameWWSFamilyName = None
        self._openTypeNameWWSSubfamilyName = None
        self._openTypeOS2CodePageRanges = None
        self._openTypeOS2FamilyClass = None
        self._openTypeOS2Panose = None
        self._openTypeOS2Selection = None
        self._openTypeOS2StrikeoutPosition = None
        self._openTypeOS2StrikeoutSize = None
        self._openTypeOS2SubscriptXOffset = None
        self._openTypeOS2SubscriptXSize = None
        self._openTypeOS2SubscriptYOffset = None
        self._openTypeOS2SubscriptYSize = None
        self._openTypeOS2SuperscriptXOffset = None
        self._openTypeOS2SuperscriptXSize = None
        self._openTypeOS2SuperscriptYOffset = None
        self._openTypeOS2SuperscriptYSize = None
        self._openTypeOS2Type = None
        self._openTypeOS2TypoAscender = None
        self._openTypeOS2TypoDescender = None
        self._openTypeOS2TypoLineGap = None
        self._openTypeOS2UnicodeRanges = None
        self._openTypeOS2VendorID = None
        self._openTypeOS2WeightClass = None
        self._openTypeOS2WidthClass = None
        self._openTypeOS2WinAscent = None
        self._openTypeOS2WinDescent = None
        self._openTypeVheaCaretOffset = None
        self._openTypeVheaCaretSlopeRise = None
        self._openTypeVheaCaretSlopeRun = None
        self._openTypeVheaVertTypoAscender = None
        self._openTypeVheaVertTypoDescender = None
        self._openTypeVheaVertTypoLineGap = None
        self._postscriptBlueFuzz = None
        self._postscriptBlueScale = None
        self._postscriptBlueShift = None
        self._postscriptBlueValues = None
        self._postscriptDefaultCharacter = None
        self._postscriptDefaultWidthX = None
        self._postscriptFamilyBlues = None
        self._postscriptFamilyOtherBlues = None
        self._postscriptFontName = None
        self._postscriptForceBold = None
        self._postscriptFullName = None
        self._postscriptIsFixedPitch = None
        self._postscriptNominalWidthX = None
        self._postscriptOtherBlues = None
        self._postscriptSlantAngle = None
        self._postscriptStemSnapH = None
        self._postscriptStemSnapV = None
        self._postscriptUnderlinePosition = None
        self._postscriptUnderlineThickness = None
        self._postscriptUniqueID = None
        self._postscriptWeightName = None
        self._postscriptWindowsCharacterSet = None
        self._styleMapFamilyName = None
        self._styleMapStyleName = None
        self._styleName = None
        self._trademark = None
        self._unitsPerEm = None
        self._versionMajor = None
        self._versionMinor = None
        self._xHeight = None
        self._year = None

    # ----------
    # Properties
    # ----------

    def _get_ascender(self):
        return self._ascender

    def _set_ascender(self, value):
        if value is None:
            self._ascender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("ascender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute ascender." % repr(value))
            else:
                self._ascender = value
        self.dirty = True

    ascender = property(_get_ascender, _set_ascender, doc="Ascender value. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_capHeight(self):
        return self._capHeight

    def _set_capHeight(self, value):
        if value is None:
            self._capHeight = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("capHeight", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute capHeight." % repr(value))
            else:
                self._capHeight = value
        self.dirty = True

    capHeight = property(_get_capHeight, _set_capHeight, doc="Cap height value. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_copyright(self):
        return self._copyright

    def _set_copyright(self, value):
        if value is None:
            self._copyright = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("copyright", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute copyright." % repr(value))
            else:
                self._copyright = value
        self.dirty = True

    copyright = property(_get_copyright, _set_copyright, doc="Copyright statement. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_descender(self):
        return self._descender

    def _set_descender(self, value):
        if value is None:
            self._descender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("descender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute descender." % repr(value))
            else:
                self._descender = value
        self.dirty = True

    descender = property(_get_descender, _set_descender, doc="Descender value. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_familyName(self):
        return self._familyName

    def _set_familyName(self, value):
        if value is None:
            self._familyName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("familyName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute familyName." % repr(value))
            else:
                self._familyName = value
        self.dirty = True

    familyName = property(_get_familyName, _set_familyName, doc="Family name. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_italicAngle(self):
        return self._italicAngle

    def _set_italicAngle(self, value):
        if value is None:
            self._italicAngle = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("italicAngle", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute italicAngle." % repr(value))
            else:
                self._italicAngle = value
        self.dirty = True

    italicAngle = property(_get_italicAngle, _set_italicAngle, doc="Italic angle. This should be a float. Setting this will post an *Info.Changed* notification.")

    def _get_macintoshFONDFamilyID(self):
        return self._macintoshFONDFamilyID

    def _set_macintoshFONDFamilyID(self, value):
        if value is None:
            self._macintoshFONDFamilyID = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("macintoshFONDFamilyID", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute macintoshFONDFamilyID." % repr(value))
            else:
                self._macintoshFONDFamilyID = value
        self.dirty = True

    macintoshFONDFamilyID = property(_get_macintoshFONDFamilyID, _set_macintoshFONDFamilyID, doc="Family ID number. Corresponds to the ffFamID in the FOND resource. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_macintoshFONDName(self):
        return self._macintoshFONDName

    def _set_macintoshFONDName(self, value):
        if value is None:
            self._macintoshFONDName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("macintoshFONDName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute macintoshFONDName." % repr(value))
            else:
                self._macintoshFONDName = value
        self.dirty = True

    macintoshFONDName = property(_get_macintoshFONDName, _set_macintoshFONDName, doc="Font name for the FOND resource. This should be a String. Setting this will post an *Info.Changed* notification.")

    def _get_note(self):
        return self._note

    def _set_note(self, value):
        if value is None:
            self._note = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("note", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute note." % repr(value))
            else:
                self._note = value
        self.dirty = True

    note = property(_get_note, _set_note, doc="Arbitrary note about the font. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHeadCreated(self):
        return self._openTypeHeadCreated

    def _set_openTypeHeadCreated(self, value):
        if value is None:
            self._openTypeHeadCreated = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHeadCreated", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHeadCreated." % repr(value))
            else:
                self._openTypeHeadCreated = value
        self.dirty = True

    openTypeHeadCreated = property(_get_openTypeHeadCreated, _set_openTypeHeadCreated, doc="Creation date. Expressed as a string of the format \"YYYY/MM/DD HH:MM:SS\". \"YYYY/MM/DD\" is year/month/day. The month should be in the range 1-12 and the day should be in the range 1-end of month. \"HH:MM:SS\" is hour:minute:second. The hour should be in the range 0:23. The minute and second should each be in the range 0-59. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHeadFlags(self):
        return self._openTypeHeadFlags

    def _set_openTypeHeadFlags(self, value):
        if value is None:
            self._openTypeHeadFlags = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHeadFlags", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHeadFlags." % repr(value))
            else:
                self._openTypeHeadFlags = value
        self.dirty = True

    openTypeHeadFlags = property(_get_openTypeHeadFlags, _set_openTypeHeadFlags, doc="A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table flags field. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHeadLowestRecPPEM(self):
        return self._openTypeHeadLowestRecPPEM

    def _set_openTypeHeadLowestRecPPEM(self, value):
        if value is None:
            self._openTypeHeadLowestRecPPEM = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHeadLowestRecPPEM", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHeadLowestRecPPEM." % repr(value))
            else:
                self._openTypeHeadLowestRecPPEM = value
        self.dirty = True

    openTypeHeadLowestRecPPEM = property(_get_openTypeHeadLowestRecPPEM, _set_openTypeHeadLowestRecPPEM, doc="Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHheaAscender(self):
        return self._openTypeHheaAscender

    def _set_openTypeHheaAscender(self, value):
        if value is None:
            self._openTypeHheaAscender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHheaAscender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHheaAscender." % repr(value))
            else:
                self._openTypeHheaAscender = value
        self.dirty = True

    openTypeHheaAscender = property(_get_openTypeHheaAscender, _set_openTypeHheaAscender, doc="Ascender value. Corresponds to the OpenType hhea table Ascender field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHheaCaretOffset(self):
        return self._openTypeHheaCaretOffset

    def _set_openTypeHheaCaretOffset(self, value):
        if value is None:
            self._openTypeHheaCaretOffset = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHheaCaretOffset", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHheaCaretOffset." % repr(value))
            else:
                self._openTypeHheaCaretOffset = value
        self.dirty = True

    openTypeHheaCaretOffset = property(_get_openTypeHheaCaretOffset, _set_openTypeHheaCaretOffset, doc="Caret offset value. Corresponds to the OpenType hhea table caretOffset field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHheaCaretSlopeRise(self):
        return self._openTypeHheaCaretSlopeRise

    def _set_openTypeHheaCaretSlopeRise(self, value):
        if value is None:
            self._openTypeHheaCaretSlopeRise = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHheaCaretSlopeRise", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHheaCaretSlopeRise." % repr(value))
            else:
                self._openTypeHheaCaretSlopeRise = value
        self.dirty = True

    openTypeHheaCaretSlopeRise = property(_get_openTypeHheaCaretSlopeRise, _set_openTypeHheaCaretSlopeRise, doc="Caret slope rise value. Corresponds to the OpenType hhea table caretSlopeRise field. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHheaCaretSlopeRun(self):
        return self._openTypeHheaCaretSlopeRun

    def _set_openTypeHheaCaretSlopeRun(self, value):
        if value is None:
            self._openTypeHheaCaretSlopeRun = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHheaCaretSlopeRun", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHheaCaretSlopeRun." % repr(value))
            else:
                self._openTypeHheaCaretSlopeRun = value
        self.dirty = True

    openTypeHheaCaretSlopeRun = property(_get_openTypeHheaCaretSlopeRun, _set_openTypeHheaCaretSlopeRun, doc="Caret slope run value. Corresponds to the OpenType hhea table caretSlopeRun field. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHheaDescender(self):
        return self._openTypeHheaDescender

    def _set_openTypeHheaDescender(self, value):
        if value is None:
            self._openTypeHheaDescender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHheaDescender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHheaDescender." % repr(value))
            else:
                self._openTypeHheaDescender = value
        self.dirty = True

    openTypeHheaDescender = property(_get_openTypeHheaDescender, _set_openTypeHheaDescender, doc="Descender value. Corresponds to the OpenType hhea table Descender field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeHheaLineGap(self):
        return self._openTypeHheaLineGap

    def _set_openTypeHheaLineGap(self, value):
        if value is None:
            self._openTypeHheaLineGap = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeHheaLineGap", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeHheaLineGap." % repr(value))
            else:
                self._openTypeHheaLineGap = value
        self.dirty = True

    openTypeHheaLineGap = property(_get_openTypeHheaLineGap, _set_openTypeHheaLineGap, doc="Line gap value. Corresponds to the OpenType hhea table LineGap field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameCompatibleFullName(self):
        return self._openTypeNameCompatibleFullName

    def _set_openTypeNameCompatibleFullName(self, value):
        if value is None:
            self._openTypeNameCompatibleFullName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameCompatibleFullName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameCompatibleFullName." % repr(value))
            else:
                self._openTypeNameCompatibleFullName = value
        self.dirty = True

    openTypeNameCompatibleFullName = property(_get_openTypeNameCompatibleFullName, _set_openTypeNameCompatibleFullName, doc="Compatible full name. Corresponds to the OpenType name table name ID 18. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameDescription(self):
        return self._openTypeNameDescription

    def _set_openTypeNameDescription(self, value):
        if value is None:
            self._openTypeNameDescription = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameDescription", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameDescription." % repr(value))
            else:
                self._openTypeNameDescription = value
        self.dirty = True

    openTypeNameDescription = property(_get_openTypeNameDescription, _set_openTypeNameDescription, doc="Description of the font. Corresponds to the OpenType name table name ID 10. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameDesigner(self):
        return self._openTypeNameDesigner

    def _set_openTypeNameDesigner(self, value):
        if value is None:
            self._openTypeNameDesigner = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameDesigner", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameDesigner." % repr(value))
            else:
                self._openTypeNameDesigner = value
        self.dirty = True

    openTypeNameDesigner = property(_get_openTypeNameDesigner, _set_openTypeNameDesigner, doc="Designer name. Corresponds to the OpenType name table name ID 9. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameDesignerURL(self):
        return self._openTypeNameDesignerURL

    def _set_openTypeNameDesignerURL(self, value):
        if value is None:
            self._openTypeNameDesignerURL = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameDesignerURL", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameDesignerURL." % repr(value))
            else:
                self._openTypeNameDesignerURL = value
        self.dirty = True

    openTypeNameDesignerURL = property(_get_openTypeNameDesignerURL, _set_openTypeNameDesignerURL, doc="URL for the designer. Corresponds to the OpenType name table name ID 12. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameLicense(self):
        return self._openTypeNameLicense

    def _set_openTypeNameLicense(self, value):
        if value is None:
            self._openTypeNameLicense = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameLicense", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameLicense." % repr(value))
            else:
                self._openTypeNameLicense = value
        self.dirty = True

    openTypeNameLicense = property(_get_openTypeNameLicense, _set_openTypeNameLicense, doc="License text. Corresponds to the OpenType name table name ID 13. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameLicenseURL(self):
        return self._openTypeNameLicenseURL

    def _set_openTypeNameLicenseURL(self, value):
        if value is None:
            self._openTypeNameLicenseURL = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameLicenseURL", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameLicenseURL." % repr(value))
            else:
                self._openTypeNameLicenseURL = value
        self.dirty = True

    openTypeNameLicenseURL = property(_get_openTypeNameLicenseURL, _set_openTypeNameLicenseURL, doc="URL for the license. Corresponds to the OpenType name table name ID 14. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameManufacturer(self):
        return self._openTypeNameManufacturer

    def _set_openTypeNameManufacturer(self, value):
        if value is None:
            self._openTypeNameManufacturer = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameManufacturer", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameManufacturer." % repr(value))
            else:
                self._openTypeNameManufacturer = value
        self.dirty = True

    openTypeNameManufacturer = property(_get_openTypeNameManufacturer, _set_openTypeNameManufacturer, doc="Manufacturer name. Corresponds to the OpenType name table name ID 8. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameManufacturerURL(self):
        return self._openTypeNameManufacturerURL

    def _set_openTypeNameManufacturerURL(self, value):
        if value is None:
            self._openTypeNameManufacturerURL = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameManufacturerURL", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameManufacturerURL." % repr(value))
            else:
                self._openTypeNameManufacturerURL = value
        self.dirty = True

    openTypeNameManufacturerURL = property(_get_openTypeNameManufacturerURL, _set_openTypeNameManufacturerURL, doc="Manufacturer URL. Corresponds to the OpenType name table name ID 11. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNamePreferredFamilyName(self):
        return self._openTypeNamePreferredFamilyName

    def _set_openTypeNamePreferredFamilyName(self, value):
        if value is None:
            self._openTypeNamePreferredFamilyName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNamePreferredFamilyName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNamePreferredFamilyName." % repr(value))
            else:
                self._openTypeNamePreferredFamilyName = value
        self.dirty = True

    openTypeNamePreferredFamilyName = property(_get_openTypeNamePreferredFamilyName, _set_openTypeNamePreferredFamilyName, doc="Preferred family name. Corresponds to the OpenType name table name ID 16. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNamePreferredSubfamilyName(self):
        return self._openTypeNamePreferredSubfamilyName

    def _set_openTypeNamePreferredSubfamilyName(self, value):
        if value is None:
            self._openTypeNamePreferredSubfamilyName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNamePreferredSubfamilyName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNamePreferredSubfamilyName." % repr(value))
            else:
                self._openTypeNamePreferredSubfamilyName = value
        self.dirty = True

    openTypeNamePreferredSubfamilyName = property(_get_openTypeNamePreferredSubfamilyName, _set_openTypeNamePreferredSubfamilyName, doc="Preferred subfamily name. Corresponds to the OpenType name table name ID 17. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameSampleText(self):
        return self._openTypeNameSampleText

    def _set_openTypeNameSampleText(self, value):
        if value is None:
            self._openTypeNameSampleText = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameSampleText", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameSampleText." % repr(value))
            else:
                self._openTypeNameSampleText = value
        self.dirty = True

    openTypeNameSampleText = property(_get_openTypeNameSampleText, _set_openTypeNameSampleText, doc="Sample text. Corresponds to the OpenType name table name ID 20. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameUniqueID(self):
        return self._openTypeNameUniqueID

    def _set_openTypeNameUniqueID(self, value):
        if value is None:
            self._openTypeNameUniqueID = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameUniqueID", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameUniqueID." % repr(value))
            else:
                self._openTypeNameUniqueID = value
        self.dirty = True

    openTypeNameUniqueID = property(_get_openTypeNameUniqueID, _set_openTypeNameUniqueID, doc="Unique ID string. Corresponds to the OpenType name table name ID 3. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameVersion(self):
        return self._openTypeNameVersion

    def _set_openTypeNameVersion(self, value):
        if value is None:
            self._openTypeNameVersion = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameVersion", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameVersion." % repr(value))
            else:
                self._openTypeNameVersion = value
        self.dirty = True

    openTypeNameVersion = property(_get_openTypeNameVersion, _set_openTypeNameVersion, doc="Version string. Corresponds to the OpenType name table name ID 5. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameWWSFamilyName(self):
        return self._openTypeNameWWSFamilyName

    def _set_openTypeNameWWSFamilyName(self, value):
        if value is None:
            self._openTypeNameWWSFamilyName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameWWSFamilyName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameWWSFamilyName." % repr(value))
            else:
                self._openTypeNameWWSFamilyName = value
        self.dirty = True

    openTypeNameWWSFamilyName = property(_get_openTypeNameWWSFamilyName, _set_openTypeNameWWSFamilyName, doc="WWS family name. Corresponds to the OpenType name table name ID 21. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeNameWWSSubfamilyName(self):
        return self._openTypeNameWWSSubfamilyName

    def _set_openTypeNameWWSSubfamilyName(self, value):
        if value is None:
            self._openTypeNameWWSSubfamilyName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeNameWWSSubfamilyName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeNameWWSSubfamilyName." % repr(value))
            else:
                self._openTypeNameWWSSubfamilyName = value
        self.dirty = True

    openTypeNameWWSSubfamilyName = property(_get_openTypeNameWWSSubfamilyName, _set_openTypeNameWWSSubfamilyName, doc="WWS Subfamily name. Corresponds to the OpenType name table name ID 22. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2CodePageRanges(self):
        return self._openTypeOS2CodePageRanges

    def _set_openTypeOS2CodePageRanges(self, value):
        if value is None:
            self._openTypeOS2CodePageRanges = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2CodePageRanges", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2CodePageRanges." % repr(value))
            else:
                self._openTypeOS2CodePageRanges = value
        self.dirty = True

    openTypeOS2CodePageRanges = property(_get_openTypeOS2CodePageRanges, _set_openTypeOS2CodePageRanges, doc="A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2FamilyClass(self):
        return self._openTypeOS2FamilyClass

    def _set_openTypeOS2FamilyClass(self, value):
        if value is None:
            self._openTypeOS2FamilyClass = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2FamilyClass", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2FamilyClass." % repr(value))
            else:
                self._openTypeOS2FamilyClass = value
        self.dirty = True

    openTypeOS2FamilyClass = property(_get_openTypeOS2FamilyClass, _set_openTypeOS2FamilyClass, doc="Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, should be in the range 0-14. The second number, representing the subclass, should be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table sFamilyClass field. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2Panose(self):
        return self._openTypeOS2Panose

    def _set_openTypeOS2Panose(self, value):
        if value is None:
            self._openTypeOS2Panose = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2Panose", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2Panose." % repr(value))
            else:
                self._openTypeOS2Panose = value
        self.dirty = True

    openTypeOS2Panose = property(_get_openTypeOS2Panose, _set_openTypeOS2Panose, doc="The list should contain 10 integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table Panose field. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2Selection(self):
        return self._openTypeOS2Selection

    def _set_openTypeOS2Selection(self, value):
        if value is None:
            self._openTypeOS2Selection = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2Selection", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2Selection." % repr(value))
            else:
                self._openTypeOS2Selection = value
        self.dirty = True

    openTypeOS2Selection = property(_get_openTypeOS2Selection, _set_openTypeOS2Selection, doc="A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table selection field. Note: Bits 0 (italic), 5 (bold) and 6 (regular) should not be set here. These bits should be taken from the generic styleMapStyle attribute. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2StrikeoutPosition(self):
        return self._openTypeOS2StrikeoutPosition

    def _set_openTypeOS2StrikeoutPosition(self, value):
        if value is None:
            self._openTypeOS2StrikeoutPosition = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2StrikeoutPosition", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2StrikeoutPosition." % repr(value))
            else:
                self._openTypeOS2StrikeoutPosition = value
        self.dirty = True

    openTypeOS2StrikeoutPosition = property(_get_openTypeOS2StrikeoutPosition, _set_openTypeOS2StrikeoutPosition, doc="Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2StrikeoutSize(self):
        return self._openTypeOS2StrikeoutSize

    def _set_openTypeOS2StrikeoutSize(self, value):
        if value is None:
            self._openTypeOS2StrikeoutSize = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2StrikeoutSize", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2StrikeoutSize." % repr(value))
            else:
                self._openTypeOS2StrikeoutSize = value
        self.dirty = True

    openTypeOS2StrikeoutSize = property(_get_openTypeOS2StrikeoutSize, _set_openTypeOS2StrikeoutSize, doc="Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SubscriptXOffset(self):
        return self._openTypeOS2SubscriptXOffset

    def _set_openTypeOS2SubscriptXOffset(self, value):
        if value is None:
            self._openTypeOS2SubscriptXOffset = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SubscriptXOffset", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SubscriptXOffset." % repr(value))
            else:
                self._openTypeOS2SubscriptXOffset = value
        self.dirty = True

    openTypeOS2SubscriptXOffset = property(_get_openTypeOS2SubscriptXOffset, _set_openTypeOS2SubscriptXOffset, doc="Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SubscriptXSize(self):
        return self._openTypeOS2SubscriptXSize

    def _set_openTypeOS2SubscriptXSize(self, value):
        if value is None:
            self._openTypeOS2SubscriptXSize = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SubscriptXSize", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SubscriptXSize." % repr(value))
            else:
                self._openTypeOS2SubscriptXSize = value
        self.dirty = True

    openTypeOS2SubscriptXSize = property(_get_openTypeOS2SubscriptXSize, _set_openTypeOS2SubscriptXSize, doc="Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SubscriptYOffset(self):
        return self._openTypeOS2SubscriptYOffset

    def _set_openTypeOS2SubscriptYOffset(self, value):
        if value is None:
            self._openTypeOS2SubscriptYOffset = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SubscriptYOffset", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SubscriptYOffset." % repr(value))
            else:
                self._openTypeOS2SubscriptYOffset = value
        self.dirty = True

    openTypeOS2SubscriptYOffset = property(_get_openTypeOS2SubscriptYOffset, _set_openTypeOS2SubscriptYOffset, doc="Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SubscriptYSize(self):
        return self._openTypeOS2SubscriptYSize

    def _set_openTypeOS2SubscriptYSize(self, value):
        if value is None:
            self._openTypeOS2SubscriptYSize = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SubscriptYSize", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SubscriptYSize." % repr(value))
            else:
                self._openTypeOS2SubscriptYSize = value
        self.dirty = True

    openTypeOS2SubscriptYSize = property(_get_openTypeOS2SubscriptYSize, _set_openTypeOS2SubscriptYSize, doc="Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SuperscriptXOffset(self):
        return self._openTypeOS2SuperscriptXOffset

    def _set_openTypeOS2SuperscriptXOffset(self, value):
        if value is None:
            self._openTypeOS2SuperscriptXOffset = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SuperscriptXOffset", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SuperscriptXOffset." % repr(value))
            else:
                self._openTypeOS2SuperscriptXOffset = value
        self.dirty = True

    openTypeOS2SuperscriptXOffset = property(_get_openTypeOS2SuperscriptXOffset, _set_openTypeOS2SuperscriptXOffset, doc="Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SuperscriptXSize(self):
        return self._openTypeOS2SuperscriptXSize

    def _set_openTypeOS2SuperscriptXSize(self, value):
        if value is None:
            self._openTypeOS2SuperscriptXSize = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SuperscriptXSize", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SuperscriptXSize." % repr(value))
            else:
                self._openTypeOS2SuperscriptXSize = value
        self.dirty = True

    openTypeOS2SuperscriptXSize = property(_get_openTypeOS2SuperscriptXSize, _set_openTypeOS2SuperscriptXSize, doc="Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SuperscriptYOffset(self):
        return self._openTypeOS2SuperscriptYOffset

    def _set_openTypeOS2SuperscriptYOffset(self, value):
        if value is None:
            self._openTypeOS2SuperscriptYOffset = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SuperscriptYOffset", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SuperscriptYOffset." % repr(value))
            else:
                self._openTypeOS2SuperscriptYOffset = value
        self.dirty = True

    openTypeOS2SuperscriptYOffset = property(_get_openTypeOS2SuperscriptYOffset, _set_openTypeOS2SuperscriptYOffset, doc="Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2SuperscriptYSize(self):
        return self._openTypeOS2SuperscriptYSize

    def _set_openTypeOS2SuperscriptYSize(self, value):
        if value is None:
            self._openTypeOS2SuperscriptYSize = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2SuperscriptYSize", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2SuperscriptYSize." % repr(value))
            else:
                self._openTypeOS2SuperscriptYSize = value
        self.dirty = True

    openTypeOS2SuperscriptYSize = property(_get_openTypeOS2SuperscriptYSize, _set_openTypeOS2SuperscriptYSize, doc="Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2Type(self):
        return self._openTypeOS2Type

    def _set_openTypeOS2Type(self, value):
        if value is None:
            self._openTypeOS2Type = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2Type", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2Type." % repr(value))
            else:
                self._openTypeOS2Type = value
        self.dirty = True

    openTypeOS2Type = property(_get_openTypeOS2Type, _set_openTypeOS2Type, doc="A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table fsType field. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2TypoAscender(self):
        return self._openTypeOS2TypoAscender

    def _set_openTypeOS2TypoAscender(self, value):
        if value is None:
            self._openTypeOS2TypoAscender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2TypoAscender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2TypoAscender." % repr(value))
            else:
                self._openTypeOS2TypoAscender = value
        self.dirty = True

    openTypeOS2TypoAscender = property(_get_openTypeOS2TypoAscender, _set_openTypeOS2TypoAscender, doc="Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2TypoDescender(self):
        return self._openTypeOS2TypoDescender

    def _set_openTypeOS2TypoDescender(self, value):
        if value is None:
            self._openTypeOS2TypoDescender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2TypoDescender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2TypoDescender." % repr(value))
            else:
                self._openTypeOS2TypoDescender = value
        self.dirty = True

    openTypeOS2TypoDescender = property(_get_openTypeOS2TypoDescender, _set_openTypeOS2TypoDescender, doc="Descender value. Corresponds to the OpenType OS/2 table sTypoDescender field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2TypoLineGap(self):
        return self._openTypeOS2TypoLineGap

    def _set_openTypeOS2TypoLineGap(self, value):
        if value is None:
            self._openTypeOS2TypoLineGap = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2TypoLineGap", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2TypoLineGap." % repr(value))
            else:
                self._openTypeOS2TypoLineGap = value
        self.dirty = True

    openTypeOS2TypoLineGap = property(_get_openTypeOS2TypoLineGap, _set_openTypeOS2TypoLineGap, doc="Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2UnicodeRanges(self):
        return self._openTypeOS2UnicodeRanges

    def _set_openTypeOS2UnicodeRanges(self, value):
        if value is None:
            self._openTypeOS2UnicodeRanges = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2UnicodeRanges", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2UnicodeRanges." % repr(value))
            else:
                self._openTypeOS2UnicodeRanges = value
        self.dirty = True

    openTypeOS2UnicodeRanges = property(_get_openTypeOS2UnicodeRanges, _set_openTypeOS2UnicodeRanges, doc="A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2VendorID(self):
        return self._openTypeOS2VendorID

    def _set_openTypeOS2VendorID(self, value):
        if value is None:
            self._openTypeOS2VendorID = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2VendorID", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2VendorID." % repr(value))
            else:
                self._openTypeOS2VendorID = value
        self.dirty = True

    openTypeOS2VendorID = property(_get_openTypeOS2VendorID, _set_openTypeOS2VendorID, doc="Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2WeightClass(self):
        return self._openTypeOS2WeightClass

    def _set_openTypeOS2WeightClass(self, value):
        if value is None:
            self._openTypeOS2WeightClass = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2WeightClass", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2WeightClass." % repr(value))
            else:
                self._openTypeOS2WeightClass = value
        self.dirty = True

    openTypeOS2WeightClass = property(_get_openTypeOS2WeightClass, _set_openTypeOS2WeightClass, doc="Weight class value. Must be a positive integer. Corresponds to the OpenType OS/2 table usWeightClass field. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2WidthClass(self):
        return self._openTypeOS2WidthClass

    def _set_openTypeOS2WidthClass(self, value):
        if value is None:
            self._openTypeOS2WidthClass = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2WidthClass", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2WidthClass." % repr(value))
            else:
                self._openTypeOS2WidthClass = value
        self.dirty = True

    openTypeOS2WidthClass = property(_get_openTypeOS2WidthClass, _set_openTypeOS2WidthClass, doc="Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table usWidthClass field. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2WinAscent(self):
        return self._openTypeOS2WinAscent

    def _set_openTypeOS2WinAscent(self, value):
        if value is None:
            self._openTypeOS2WinAscent = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2WinAscent", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2WinAscent." % repr(value))
            else:
                self._openTypeOS2WinAscent = value
        self.dirty = True

    openTypeOS2WinAscent = property(_get_openTypeOS2WinAscent, _set_openTypeOS2WinAscent, doc="Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeOS2WinDescent(self):
        return self._openTypeOS2WinDescent

    def _set_openTypeOS2WinDescent(self, value):
        if value is None:
            self._openTypeOS2WinDescent = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeOS2WinDescent", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeOS2WinDescent." % repr(value))
            else:
                self._openTypeOS2WinDescent = value
        self.dirty = True

    openTypeOS2WinDescent = property(_get_openTypeOS2WinDescent, _set_openTypeOS2WinDescent, doc="Descender value. Corresponds to the OpenType OS/2 table usWinDescent field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeVheaCaretOffset(self):
        return self._openTypeVheaCaretOffset

    def _set_openTypeVheaCaretOffset(self, value):
        if value is None:
            self._openTypeVheaCaretOffset = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeVheaCaretOffset", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeVheaCaretOffset." % repr(value))
            else:
                self._openTypeVheaCaretOffset = value
        self.dirty = True

    openTypeVheaCaretOffset = property(_get_openTypeVheaCaretOffset, _set_openTypeVheaCaretOffset, doc="Caret offset value. Corresponds to the OpenType vhea table caretOffset field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeVheaCaretSlopeRise(self):
        return self._openTypeVheaCaretSlopeRise

    def _set_openTypeVheaCaretSlopeRise(self, value):
        if value is None:
            self._openTypeVheaCaretSlopeRise = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeVheaCaretSlopeRise", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeVheaCaretSlopeRise." % repr(value))
            else:
                self._openTypeVheaCaretSlopeRise = value
        self.dirty = True

    openTypeVheaCaretSlopeRise = property(_get_openTypeVheaCaretSlopeRise, _set_openTypeVheaCaretSlopeRise, doc="Caret slope rise value. Corresponds to the OpenType vhea table caretSlopeRise field. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeVheaCaretSlopeRun(self):
        return self._openTypeVheaCaretSlopeRun

    def _set_openTypeVheaCaretSlopeRun(self, value):
        if value is None:
            self._openTypeVheaCaretSlopeRun = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeVheaCaretSlopeRun", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeVheaCaretSlopeRun." % repr(value))
            else:
                self._openTypeVheaCaretSlopeRun = value
        self.dirty = True

    openTypeVheaCaretSlopeRun = property(_get_openTypeVheaCaretSlopeRun, _set_openTypeVheaCaretSlopeRun, doc="Caret slope run value. Corresponds to the OpenType vhea table caretSlopeRun field. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeVheaVertTypoAscender(self):
        return self._openTypeVheaVertTypoAscender

    def _set_openTypeVheaVertTypoAscender(self, value):
        if value is None:
            self._openTypeVheaVertTypoAscender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeVheaVertTypoAscender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeVheaVertTypoAscender." % repr(value))
            else:
                self._openTypeVheaVertTypoAscender = value
        self.dirty = True

    openTypeVheaVertTypoAscender = property(_get_openTypeVheaVertTypoAscender, _set_openTypeVheaVertTypoAscender, doc="Ascender value. Corresponds to the OpenType vhea table vertTypoAscender field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeVheaVertTypoDescender(self):
        return self._openTypeVheaVertTypoDescender

    def _set_openTypeVheaVertTypoDescender(self, value):
        if value is None:
            self._openTypeVheaVertTypoDescender = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeVheaVertTypoDescender", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeVheaVertTypoDescender." % repr(value))
            else:
                self._openTypeVheaVertTypoDescender = value
        self.dirty = True

    openTypeVheaVertTypoDescender = property(_get_openTypeVheaVertTypoDescender, _set_openTypeVheaVertTypoDescender, doc="Descender value. Corresponds to the OpenType vhea table vertTypoDescender field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_openTypeVheaVertTypoLineGap(self):
        return self._openTypeVheaVertTypoLineGap

    def _set_openTypeVheaVertTypoLineGap(self, value):
        if value is None:
            self._openTypeVheaVertTypoLineGap = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("openTypeVheaVertTypoLineGap", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute openTypeVheaVertTypoLineGap." % repr(value))
            else:
                self._openTypeVheaVertTypoLineGap = value
        self.dirty = True

    openTypeVheaVertTypoLineGap = property(_get_openTypeVheaVertTypoLineGap, _set_openTypeVheaVertTypoLineGap, doc="Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptBlueFuzz(self):
        return self._postscriptBlueFuzz

    def _set_postscriptBlueFuzz(self, value):
        if value is None:
            self._postscriptBlueFuzz = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptBlueFuzz", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptBlueFuzz." % repr(value))
            else:
                self._postscriptBlueFuzz = value
        self.dirty = True

    postscriptBlueFuzz = property(_get_postscriptBlueFuzz, _set_postscriptBlueFuzz, doc="BlueFuzz value. This corresponds to the Type 1/CFF BlueFuzz field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptBlueScale(self):
        return self._postscriptBlueScale

    def _set_postscriptBlueScale(self, value):
        if value is None:
            self._postscriptBlueScale = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptBlueScale", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptBlueScale." % repr(value))
            else:
                self._postscriptBlueScale = value
        self.dirty = True

    postscriptBlueScale = property(_get_postscriptBlueScale, _set_postscriptBlueScale, doc="BlueScale value. This corresponds to the Type 1/CFF BlueScale field. This should be a float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptBlueShift(self):
        return self._postscriptBlueShift

    def _set_postscriptBlueShift(self, value):
        if value is None:
            self._postscriptBlueShift = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptBlueShift", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptBlueShift." % repr(value))
            else:
                self._postscriptBlueShift = value
        self.dirty = True

    postscriptBlueShift = property(_get_postscriptBlueShift, _set_postscriptBlueShift, doc="BlueShift value. This corresponds to the Type 1/CFF BlueShift field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptBlueValues(self):
        if self._postscriptBlueValues is None:
            return []
        return self._postscriptBlueValues

    def _set_postscriptBlueValues(self, value):
        if value is None:
            self._postscriptBlueValues = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptBlueValues", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptBlueValues." % repr(value))
            else:
                self._postscriptBlueValues = value
        self.dirty = True

    postscriptBlueValues = property(_get_postscriptBlueValues, _set_postscriptBlueValues, doc="A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptDefaultCharacter(self):
        return self._postscriptDefaultCharacter

    def _set_postscriptDefaultCharacter(self, value):
        if value is None:
            self._postscriptDefaultCharacter = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptDefaultCharacter", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptDefaultCharacter." % repr(value))
            else:
                self._postscriptDefaultCharacter = value
        self.dirty = True

    postscriptDefaultCharacter = property(_get_postscriptDefaultCharacter, _set_postscriptDefaultCharacter, doc="The name of the glyph that should be used as the default character in PFM files. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptDefaultWidthX(self):
        return self._postscriptDefaultWidthX

    def _set_postscriptDefaultWidthX(self, value):
        if value is None:
            self._postscriptDefaultWidthX = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptDefaultWidthX", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptDefaultWidthX." % repr(value))
            else:
                self._postscriptDefaultWidthX = value
        self.dirty = True

    postscriptDefaultWidthX = property(_get_postscriptDefaultWidthX, _set_postscriptDefaultWidthX, doc="Default width for glyphs. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptFamilyBlues(self):
        if self._postscriptFamilyBlues is None:
            return []
        return self._postscriptFamilyBlues

    def _set_postscriptFamilyBlues(self, value):
        if value is None:
            self._postscriptFamilyBlues = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptFamilyBlues", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptFamilyBlues." % repr(value))
            else:
                self._postscriptFamilyBlues = value
        self.dirty = True

    postscriptFamilyBlues = property(_get_postscriptFamilyBlues, _set_postscriptFamilyBlues, doc="A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptFamilyOtherBlues(self):
        if self._postscriptFamilyOtherBlues is None:
            return []
        return self._postscriptFamilyOtherBlues

    def _set_postscriptFamilyOtherBlues(self, value):
        if value is None:
            self._postscriptFamilyOtherBlues = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptFamilyOtherBlues", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptFamilyOtherBlues." % repr(value))
            else:
                self._postscriptFamilyOtherBlues = value
        self.dirty = True

    postscriptFamilyOtherBlues = property(_get_postscriptFamilyOtherBlues, _set_postscriptFamilyOtherBlues, doc="A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptFontName(self):
        return self._postscriptFontName

    def _set_postscriptFontName(self, value):
        if value is None:
            self._postscriptFontName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptFontName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptFontName." % repr(value))
            else:
                self._postscriptFontName = value
        self.dirty = True

    postscriptFontName = property(_get_postscriptFontName, _set_postscriptFontName, doc="Name to be used for the FontName field in Type 1/CFF table. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptForceBold(self):
        return self._postscriptForceBold

    def _set_postscriptForceBold(self, value):
        if value is None:
            self._postscriptForceBold = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptForceBold", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptForceBold." % repr(value))
            else:
                self._postscriptForceBold = value
        self.dirty = True

    postscriptForceBold = property(_get_postscriptForceBold, _set_postscriptForceBold, doc="Indicates how the Type 1/CFF ForceBold field should be set. This should be a boolean. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptFullName(self):
        return self._postscriptFullName

    def _set_postscriptFullName(self, value):
        if value is None:
            self._postscriptFullName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptFullName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptFullName." % repr(value))
            else:
                self._postscriptFullName = value
        self.dirty = True

    postscriptFullName = property(_get_postscriptFullName, _set_postscriptFullName, doc="Name to be used for the FullName field in Type 1/CFF table. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptIsFixedPitch(self):
        return self._postscriptIsFixedPitch

    def _set_postscriptIsFixedPitch(self, value):
        if value is None:
            self._postscriptIsFixedPitch = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptIsFixedPitch", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptIsFixedPitch." % repr(value))
            else:
                self._postscriptIsFixedPitch = value
        self.dirty = True

    postscriptIsFixedPitch = property(_get_postscriptIsFixedPitch, _set_postscriptIsFixedPitch, doc="Indicates if the font is monospaced. A compiler could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF isFixedPitched field This should be a boolean. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptNominalWidthX(self):
        return self._postscriptNominalWidthX

    def _set_postscriptNominalWidthX(self, value):
        if value is None:
            self._postscriptNominalWidthX = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptNominalWidthX", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptNominalWidthX." % repr(value))
            else:
                self._postscriptNominalWidthX = value
        self.dirty = True

    postscriptNominalWidthX = property(_get_postscriptNominalWidthX, _set_postscriptNominalWidthX, doc="Nominal width for glyphs. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptOtherBlues(self):
        if self._postscriptOtherBlues is None:
            return []
        return self._postscriptOtherBlues

    def _set_postscriptOtherBlues(self, value):
        if value is None:
            self._postscriptOtherBlues = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptOtherBlues", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptOtherBlues." % repr(value))
            else:
                self._postscriptOtherBlues = value
        self.dirty = True

    postscriptOtherBlues = property(_get_postscriptOtherBlues, _set_postscriptOtherBlues, doc="A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptSlantAngle(self):
        return self._postscriptSlantAngle

    def _set_postscriptSlantAngle(self, value):
        if value is None:
            self._postscriptSlantAngle = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptSlantAngle", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptSlantAngle." % repr(value))
            else:
                self._postscriptSlantAngle = value
        self.dirty = True

    postscriptSlantAngle = property(_get_postscriptSlantAngle, _set_postscriptSlantAngle, doc="Artificial slant angle. This should be a float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptStemSnapH(self):
        if self._postscriptStemSnapH is None:
            return []
        return self._postscriptStemSnapH

    def _set_postscriptStemSnapH(self, value):
        if value is None:
            self._postscriptStemSnapH = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptStemSnapH", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptStemSnapH." % repr(value))
            else:
                self._postscriptStemSnapH = value
        self.dirty = True

    postscriptStemSnapH = property(_get_postscriptStemSnapH, _set_postscriptStemSnapH, doc="List of horizontal stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapH field. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptStemSnapV(self):
        if self._postscriptStemSnapV is None:
            return []
        return self._postscriptStemSnapV

    def _set_postscriptStemSnapV(self, value):
        if value is None:
            self._postscriptStemSnapV = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptStemSnapV", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptStemSnapV." % repr(value))
            else:
                self._postscriptStemSnapV = value
        self.dirty = True

    postscriptStemSnapV = property(_get_postscriptStemSnapV, _set_postscriptStemSnapV, doc="List of vertical stems sorted in increasing order. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapV field. This should be a number list. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptUnderlinePosition(self):
        return self._postscriptUnderlinePosition

    def _set_postscriptUnderlinePosition(self, value):
        if value is None:
            self._postscriptUnderlinePosition = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptUnderlinePosition", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptUnderlinePosition." % repr(value))
            else:
                self._postscriptUnderlinePosition = value
        self.dirty = True

    postscriptUnderlinePosition = property(_get_postscriptUnderlinePosition, _set_postscriptUnderlinePosition, doc="Underline position value. Corresponds to the Type 1/CFF/post table UnderlinePosition field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptUnderlineThickness(self):
        return self._postscriptUnderlineThickness

    def _set_postscriptUnderlineThickness(self, value):
        if value is None:
            self._postscriptUnderlineThickness = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptUnderlineThickness", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptUnderlineThickness." % repr(value))
            else:
                self._postscriptUnderlineThickness = value
        self.dirty = True

    postscriptUnderlineThickness = property(_get_postscriptUnderlineThickness, _set_postscriptUnderlineThickness, doc="Underline thickness value. Corresponds to the Type 1/CFF/post table UnderlineThickness field. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptUniqueID(self):
        return self._postscriptUniqueID

    def _set_postscriptUniqueID(self, value):
        if value is None:
            self._postscriptUniqueID = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptUniqueID", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptUniqueID." % repr(value))
            else:
                self._postscriptUniqueID = value
        self.dirty = True

    postscriptUniqueID = property(_get_postscriptUniqueID, _set_postscriptUniqueID, doc="A unique ID number as defined in the Type 1/CFF specification. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptWeightName(self):
        return self._postscriptWeightName

    def _set_postscriptWeightName(self, value):
        if value is None:
            self._postscriptWeightName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptWeightName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptWeightName." % repr(value))
            else:
                self._postscriptWeightName = value
        self.dirty = True

    postscriptWeightName = property(_get_postscriptWeightName, _set_postscriptWeightName, doc="A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the openTypeOS2WeightClass value. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_postscriptWindowsCharacterSet(self):
        return self._postscriptWindowsCharacterSet

    def _set_postscriptWindowsCharacterSet(self, value):
        if value is None:
            self._postscriptWindowsCharacterSet = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("postscriptWindowsCharacterSet", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute postscriptWindowsCharacterSet." % repr(value))
            else:
                self._postscriptWindowsCharacterSet = value
        self.dirty = True

    postscriptWindowsCharacterSet = property(_get_postscriptWindowsCharacterSet, _set_postscriptWindowsCharacterSet, doc="The Windows character set. The values are defined below. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_styleMapFamilyName(self):
        return self._styleMapFamilyName

    def _set_styleMapFamilyName(self, value):
        if value is None:
            self._styleMapFamilyName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("styleMapFamilyName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute styleMapFamilyName." % repr(value))
            else:
                self._styleMapFamilyName = value
        self.dirty = True

    styleMapFamilyName = property(_get_styleMapFamilyName, _set_styleMapFamilyName, doc="Family name used for bold, italic and bold italic style mapping. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_styleMapStyleName(self):
        return self._styleMapStyleName

    def _set_styleMapStyleName(self, value):
        if value is None:
            self._styleMapStyleName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("styleMapStyleName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute styleMapStyleName." % repr(value))
            else:
                self._styleMapStyleName = value
        self.dirty = True

    styleMapStyleName = property(_get_styleMapStyleName, _set_styleMapStyleName, doc="Style map style. The possible values are regular, italic, bold and bold italic. These are case sensitive. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_styleName(self):
        return self._styleName

    def _set_styleName(self, value):
        if value is None:
            self._styleName = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("styleName", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute styleName." % repr(value))
            else:
                self._styleName = value
        self.dirty = True

    styleName = property(_get_styleName, _set_styleName, doc="Style name. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_trademark(self):
        return self._trademark

    def _set_trademark(self, value):
        if value is None:
            self._trademark = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("trademark", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute trademark." % repr(value))
            else:
                self._trademark = value
        self.dirty = True

    trademark = property(_get_trademark, _set_trademark, doc="Trademark statement. This should be a string. Setting this will post an *Info.Changed* notification.")

    def _get_unitsPerEm(self):
        return self._unitsPerEm

    def _set_unitsPerEm(self, value):
        if value is None:
            self._unitsPerEm = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("unitsPerEm", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute unitsPerEm." % repr(value))
            else:
                self._unitsPerEm = value
        self.dirty = True

    unitsPerEm = property(_get_unitsPerEm, _set_unitsPerEm, doc="Units per em. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_versionMajor(self):
        return self._versionMajor

    def _set_versionMajor(self, value):
        if value is None:
            self._versionMajor = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("versionMajor", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute versionMajor." % repr(value))
            else:
                self._versionMajor = value
        self.dirty = True

    versionMajor = property(_get_versionMajor, _set_versionMajor, doc="Major version. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_versionMinor(self):
        return self._versionMinor

    def _set_versionMinor(self, value):
        if value is None:
            self._versionMinor = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("versionMinor", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute versionMinor." % repr(value))
            else:
                self._versionMinor = value
        self.dirty = True

    versionMinor = property(_get_versionMinor, _set_versionMinor, doc="Minor version. This should be a integer. Setting this will post an *Info.Changed* notification.")

    def _get_xHeight(self):
        return self._xHeight

    def _set_xHeight(self, value):
        if value is None:
            self._xHeight = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("xHeight", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute xHeight." % repr(value))
            else:
                self._xHeight = value
        self.dirty = True

    xHeight = property(_get_xHeight, _set_xHeight, doc="x-height value. This should be a integer or float. Setting this will post an *Info.Changed* notification.")

    def _get_year(self):
        return self._year

    def _set_year(self, value):
        if value is None:
            self._year = None
        else:
            valid = ufoLib.validateFontInfoVersion2ValueForAttribute("year", value)
            if not valid:
                raise ValueError("Invalid value (%s) for attribute year." % repr(value))
            else:
                self._year = value
        self.dirty = True

    year = property(_get_year, _set_year, doc="The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by applications. However, it may occur in a font's info so applications should preserve it if present. This should be a integer. Setting this will post an *Info.Changed* notification.")

    # ----
    # Undo
    # ----

    def getDataToSerializeForUndo(self):
        data = dict.fromkeys(ufoLib.fontInfoAttributesVersion2)
        for attr in data.keys():
            data[attr] = getattr(self, attr)
        return data

    def loadDeserializedDataFromUndo(self, data):
        for attr, value in data.items():
            if getattr(self, attr) == value:
                continue
            setattr(self, attr, value)

