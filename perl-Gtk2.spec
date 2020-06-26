%define	modname	Gtk2
%define modver 1.24993

Summary:	Perl module for the gtk+-2.x library

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2 or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://sourceforge.net/projects/gtk2-perl/files/%{modname}/%{modver}/%{modname}-%{modver}.tar.gz
Source1:	perl-Gtk2.rpmlintrc
Patch7:		Gtk2-1.244-gtk_exit.patch
Patch21:	Gtk2-1.038-xset_input_focus.patch
Patch23:	Gtk2-1.023-exception-trapping.patch
Patch26:  Gtk2-perl-5.20.diff

BuildRequires:	perl(Cairo)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib)
BuildRequires:	perl(Pango)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	perl-devel
# for test suite:
BuildRequires:	perl(Test::More)
BuildRequires:	fontconfig
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	x11-server-xvfb
Requires:	gtk+2
#	(misc) needed by /usr/lib/perl5/vendor_perl/5.8.7/i386-linux/Gtk2/Install/Files.pm
Requires:	perl(Cairo)
Requires:   perl-Glib
# needed by /usr/lib/perl5/vendor_perl/5.8.7/i386-linux/Gtk2/Install/Files.pm
Requires:   perl-Cairo
Requires:   perl-Pango
# required to avoid warnings when loading
Recommends:	canberra-gtk
# libegg's code for status icon was merged in gtk+2.9.x:
Provides:	perl-Gtk2-StatusIcon = %{version}-%{release}
Obsoletes:	perl-Gtk2-StatusIcon <= 0.010

# Be sure to update this list on any upstream change
Provides: perl(Gtk2)
Provides: perl(Gtk2::AboutDialog)
Provides: perl(Gtk2::AccelGroup)
Provides: perl(Gtk2::AccelLabel)
Provides: perl(Gtk2::AccelMap)
Provides: perl(Gtk2::Action)
Provides: perl(Gtk2::ActionGroup)
Provides: perl(Gtk2::Activatable)
Provides: perl(Gtk2::Adjustment)
Provides: perl(Gtk2::Alignment)
Provides: perl(Gtk2::Arrow)
Provides: perl(Gtk2::AspectFrame)
Provides: perl(Gtk2::Assistant)
Provides: perl(Gtk2::Bin)
Provides: perl(Gtk2::BindingSet)
Provides: perl(Gtk2::Box)
Provides: perl(Gtk2::Buildable)
Provides: perl(Gtk2::Builder)
Provides: perl(Gtk2::Button)
Provides: perl(Gtk2::ButtonBox)
Provides: perl(Gtk2::Calendar)
Provides: perl(Gtk2::CellEditable)
Provides: perl(Gtk2::CellLayout)
Provides: perl(Gtk2::CellRenderer)
Provides: perl(Gtk2::CellRendererAccel)
Provides: perl(Gtk2::CellRendererCombo)
Provides: perl(Gtk2::CellRendererPixbuf)
Provides: perl(Gtk2::CellRendererProgress)
Provides: perl(Gtk2::CellRendererSpin)
Provides: perl(Gtk2::CellRendererSpinner)
Provides: perl(Gtk2::CellRendererText)
Provides: perl(Gtk2::CellRendererToggle)
Provides: perl(Gtk2::CellView)
Provides: perl(Gtk2::CheckButton)
Provides: perl(Gtk2::CheckMenuItem)
Provides: perl(Gtk2::Clipboard)
Provides: perl(Gtk2::ColorButton)
Provides: perl(Gtk2::ColorSelection)
Provides: perl(Gtk2::ColorSelectionDialog)
Provides: perl(Gtk2::Combo)
Provides: perl(Gtk2::ComboBox)
Provides: perl(Gtk2::ComboBoxEntry)
Provides: perl(Gtk2::Container)
Provides: perl(Gtk2::Curve)
Provides: perl(Gtk2::Dialog)
Provides: perl(Gtk2::Dnd)
Provides: perl(Gtk2::DrawingArea)
Provides: perl(Gtk2::Editable)
Provides: perl(Gtk2::Entry)
Provides: perl(Gtk2::EntryBuffer)
Provides: perl(Gtk2::EntryCompletion)
Provides: perl(Gtk2::EventBox)
Provides: perl(Gtk2::Expander)
Provides: perl(Gtk2::FileChooser)
Provides: perl(Gtk2::FileChooserButton)
Provides: perl(Gtk2::FileChooserDialog)
Provides: perl(Gtk2::FileChooserWidget)
Provides: perl(Gtk2::FileFilter)
Provides: perl(Gtk2::FileSelection)
Provides: perl(Gtk2::Fixed)
Provides: perl(Gtk2::FontButton)
Provides: perl(Gtk2::FontSelection)
Provides: perl(Gtk2::Frame)
Provides: perl(Gtk2::GammaCurve)
Provides: perl(Gtk2::GC)
Provides: perl(Gtk2::Gdk)
Provides: perl(Gtk2::Gdk::Cairo)
Provides: perl(Gtk2::Gdk::Color)
Provides: perl(Gtk2::Gdk::Cursor)
Provides: perl(Gtk2::Gdk::Device)
Provides: perl(Gtk2::Gdk::Display)
Provides: perl(Gtk2::Gdk::DisplayManager)
Provides: perl(Gtk2::Gdk::Dnd)
Provides: perl(Gtk2::Gdk::Drawable)
Provides: perl(Gtk2::Gdk::Event)
Provides: perl(Gtk2::Gdk::GC)
Provides: perl(Gtk2::Gdk::Image)
Provides: perl(Gtk2::Gdk::Keys)
Provides: perl(Gtk2::Gdk::Pango)
Provides: perl(Gtk2::Gdk::Pixbuf)
Provides: perl(Gtk2::Gdk::PixbufLoader)
Provides: perl(Gtk2::Gdk::PixbufSimpleAnim)
Provides: perl(Gtk2::Gdk::Pixmap)
Provides: perl(Gtk2::Gdk::Property)
Provides: perl(Gtk2::Gdk::Region)
Provides: perl(Gtk2::Gdk::Rgb)
Provides: perl(Gtk2::Gdk::Screen)
Provides: perl(Gtk2::Gdk::Selection)
Provides: perl(Gtk2::Gdk::Types)
Provides: perl(Gtk2::Gdk::Visual)
Provides: perl(Gtk2::Gdk::Window)
Provides: perl(Gtk2::Gdk::X11)
Provides: perl(Gtk2::HandleBox)
Provides: perl(Gtk2::HBox)
Provides: perl(Gtk2::HButtonBox)
Provides: perl(Gtk2::HPaned)
Provides: perl(Gtk2::HRuler)
Provides: perl(Gtk2::HScale)
Provides: perl(Gtk2::HScrollbar)
Provides: perl(Gtk2::HSeparator)
Provides: perl(Gtk2::HSV)
Provides: perl(Gtk2::IconFactory)
Provides: perl(Gtk2::IconTheme)
Provides: perl(Gtk2::IconView)
Provides: perl(Gtk2::Image)
Provides: perl(Gtk2::ImageMenuItem)
Provides: perl(Gtk2::IMContext)
Provides: perl(Gtk2::IMContextSimple)
Provides: perl(Gtk2::IMMultiContext)
Provides: perl(Gtk2::InfoBar)
Provides: perl(Gtk2::InputDialog)
Provides: perl(Gtk2::Invisible)
Provides: perl(Gtk2::Item)
Provides: perl(Gtk2::ItemFactory)
Provides: perl(Gtk2::Label)
Provides: perl(Gtk2::Layout)
Provides: perl(Gtk2::LinkButton)
Provides: perl(Gtk2::List)
Provides: perl(Gtk2::ListItem)
Provides: perl(Gtk2::ListStore)
Provides: perl(Gtk2::Menu)
Provides: perl(Gtk2::MenuBar)
Provides: perl(Gtk2::MenuItem)
Provides: perl(Gtk2::MenuShell)
Provides: perl(Gtk2::MenuToolButton)
Provides: perl(Gtk2::MessageDialog)
Provides: perl(Gtk2::Misc)
Provides: perl(Gtk2::Notebook)
Provides: perl(Gtk2::Object)
Provides: perl(Gtk2::OffscreenWindow)
Provides: perl(Gtk2::OptionMenu)
Provides: perl(Gtk2::Orientable)
Provides: perl(Gtk2::PageSetup)
Provides: perl(Gtk2::Paned)
Provides: perl(Gtk2::PaperSize)
Provides: perl(Gtk2::Plug)
Provides: perl(Gtk2::PrintContext)
Provides: perl(Gtk2::PrintOperation)
Provides: perl(Gtk2::PrintOperationPreview)
Provides: perl(Gtk2::PrintSettings)
Provides: perl(Gtk2::ProgressBar)
Provides: perl(Gtk2::RadioAction)
Provides: perl(Gtk2::RadioButton)
Provides: perl(Gtk2::RadioMenuItem)
Provides: perl(Gtk2::RadioToolButton)
Provides: perl(Gtk2::Range)
Provides: perl(Gtk2::Rc)
Provides: perl(Gtk2::RecentAction)
Provides: perl(Gtk2::RecentChooser)
Provides: perl(Gtk2::RecentChooserDialog)
Provides: perl(Gtk2::RecentChooserMenu)
Provides: perl(Gtk2::RecentChooserWidget)
Provides: perl(Gtk2::RecentFilter)
Provides: perl(Gtk2::RecentManager)
Provides: perl(Gtk2::Ruler)
Provides: perl(Gtk2::Scale)
Provides: perl(Gtk2::ScaleButton)
Provides: perl(Gtk2::ScrolledWindow)
Provides: perl(Gtk2::Selection)
Provides: perl(Gtk2::SeparatorMenuItem)
Provides: perl(Gtk2::SeparatorToolItem)
Provides: perl(Gtk2::Show)
Provides: perl(Gtk2::SizeGroup)
Provides: perl(Gtk2::Socket)
Provides: perl(Gtk2::SpinButton)
Provides: perl(Gtk2::Spinner)
Provides: perl(Gtk2::Statusbar)
Provides: perl(Gtk2::StatusIcon)
Provides: perl(Gtk2::Stock)
Provides: perl(Gtk2::Style)
Provides: perl(Gtk2::Table)
Provides: perl(Gtk2::TearoffMenuItem)
Provides: perl(Gtk2::TextBuffer)
Provides: perl(Gtk2::TextBufferRichText)
Provides: perl(Gtk2::TextChildAnchor)
Provides: perl(Gtk2::TextIter)
Provides: perl(Gtk2::TextMark)
Provides: perl(Gtk2::TextTag)
Provides: perl(Gtk2::TextTagTable)
Provides: perl(Gtk2::TextView)
Provides: perl(Gtk2::ToggleAction)
Provides: perl(Gtk2::ToggleButton)
Provides: perl(Gtk2::ToggleToolButton)
Provides: perl(Gtk2::Toolbar)
Provides: perl(Gtk2::ToolButton)
Provides: perl(Gtk2::ToolItem)
Provides: perl(Gtk2::ToolItemGroup)
Provides: perl(Gtk2::ToolPalette)
Provides: perl(Gtk2::ToolShell)
Provides: perl(Gtk2::Tooltip)
Provides: perl(Gtk2::Tooltips)
Provides: perl(Gtk2::TreeDnd)
Provides: perl(Gtk2::TreeModel)
Provides: perl(Gtk2::TreeModelFilter)
Provides: perl(Gtk2::TreeModelSort)
Provides: perl(Gtk2::TreeSelection)
Provides: perl(Gtk2::TreeSortable)
Provides: perl(Gtk2::TreeStore)
Provides: perl(Gtk2::TreeView)
Provides: perl(Gtk2::TreeViewColumn)
Provides: perl(Gtk2::UIManager)
Provides: perl(Gtk2::VBox)
Provides: perl(Gtk2::VButtonBox)
Provides: perl(Gtk2::Viewport)
Provides: perl(Gtk2::VolumeButton)
Provides: perl(Gtk2::VPaned)
Provides: perl(Gtk2::VRuler)
Provides: perl(Gtk2::VScale)
Provides: perl(Gtk2::VScrollbar)
Provides: perl(Gtk2::VSeparator)
Provides: perl(Gtk2::Widget)
Provides: perl(Gtk2::Window)

%description
This module provides perl access to the gtk+-2.x library.

Gtk+ is the GIMP ToolKit (GTK+), a library for creating graphical user
interfaces for the X Window System.  GTK+ was originally written for the GIMP
(GNU Image Manipulation Program) image processing program, but is now used by
several other programs as well.

%package doc
Summary:	Gtk2 documentation

Group:		Books/Computer books

%description	doc
This package contains documentation of the Gtk2 module.

%prep
%setup -qn %{modname}-%{modver}
%patch7 -p1 -b .gtk_exit~
%patch21 -p0 -b .tv~
%patch23 -p0 -b .except~
chmod 755 gtk-demo/*.pl examples/*.pl
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1

%build
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc AUTHORS LICENSE META.yml NEWS README TODO
%{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}.pm
%exclude %{perl_vendorarch}/%{modname}/*.pod
%exclude %{perl_vendorarch}/%{modname}/*/*.pod
%exclude %{perl_vendorarch}/%{modname}/*/*/*.pod
%{perl_vendorarch}/auto/*

%files doc
%doc gtk-demo examples
%{perl_vendorarch}/%{modname}/*.pod
%{perl_vendorarch}/%{modname}/*/*.pod
%{perl_vendorarch}/%{modname}/*/*/*.pod
%{_mandir}/man3/*


