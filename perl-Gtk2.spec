%define	modname	Gtk2
%define	modver	1.244

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5

Summary:	Perl module for the gtk+-2.x library
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{modname}-%{modver}.tar.gz
Patch7:		Gtk2-1.244-gtk_exit.patch
Patch21:	Gtk2-1.038-xset_input_focus.patch
Patch23:	Gtk2-1.023-exception-trapping.patch 

BuildRequires:	perl(Cairo) >= 1.0.0
BuildRequires:	perl(ExtUtils::Depends) >= 0.300.0
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.120
BuildRequires:	perl(Glib) >= 1.240.0
BuildRequires:	perl(Pango) >= 1.220.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	perl-devel
# for test suite:
BuildRequires:	fontconfig
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	x11-server-xvfb
Requires:	gtk+2
Requires:	perl(Glib)
#	(misc) needed by /usr/lib/perl5/vendor_perl/5.8.7/i386-linux/Gtk2/Install/Files.pm
Requires:	perl(Cairo)
Requires:	perl(Pango)
# required to avoid warnings when loading
Suggests:	canberra-gtk
# (tv) libegg's code for status icon was merged in gtk+2.9.x:
Provides:	perl-Gtk2-StatusIcon = %{version}-%{release}
Obsoletes:	perl-Gtk2-StatusIcon <= 0.010

%description
This module provides perl access to the gtk+-2.x library.

Gtk+ is the GIMP ToolKit (GTK+), a library for creating graphical user
interfaces for the X Window System.  GTK+ was originally written for the GIMP
(GNU Image Manipulation Program) image processing program, but is now used by
several other programs as well.

%package	doc
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

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#xvfb-run %make test

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE META.yml NEWS README TODO
%{perl_vendorarch}/%{modname}/
%{perl_vendorarch}/%{modname}.pm
%exclude %{perl_vendorarch}/%{modname}/*.pod
%exclude %{perl_vendorarch}/%{modname}/*/*.pod
%exclude %{perl_vendorarch}/%{modname}/*/*/*.pod
%{perl_vendorarch}/auto/*

%files doc
%doc gtk-demo examples
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}/*.pod
%{perl_vendorarch}/%{modname}/*/*.pod
%{perl_vendorarch}/%{modname}/*/*/*.pod

%changelog
* Wed Dec 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.244.0-5
- rebuild for perl-5.16.2
- doc subpackage shouldn't be noarch as it's files are located in arch
  specific paths
- cleanups

* Fri Jun 08 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.244.0-1
+ Revision: 803636
- regenerate P7
- filter out all deps from %%{_docdir}
- drop explicit libgtk+2 dependency
- don't package examples in both packages
- filter out perl(Gtk2::ScrolledWindow) as well
- filter out dependency on perl(Gtk2::HBox)
- fix %%files
- clean up spec and drop some ancient conflicts & obsoletes..
- sync with 1.244-1 from mageia

* Mon Jan 23 2012 Götz Waschk <waschk@mandriva.org> 1.232.0-5
+ Revision: 767041
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Wed Nov 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.232.0-2
+ Revision: 735514
- rebuild for breakage with gtk+2.0
- removed old obsoletes requires provides conflicts
- cleaned up spec
- remove mkrel, BuildRoot, clean section, defattr

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.232.0-1
+ Revision: 702809
- 1.230

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-7
+ Revision: 702776
- rebuilt against libpng-1.5.x
