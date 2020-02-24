%define	modname	Gtk2
%define modver 1.24992

Summary:	Perl module for the gtk+-2.x library

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2 or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://sourceforge.net/projects/gtk2-perl/files/%{modname}/%{modver}/%{modname}-%{modver}.tar.gz
Source1:	perl-Gtk2.rpmlintrc
Patch7:		Gtk2-1.244-gtk_exit.patch
Patch21:	Gtk2-1.038-xset_input_focus.patch
Patch23:	Gtk2-1.023-exception-trapping.patch 

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

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
#xvfb-run %make test

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


