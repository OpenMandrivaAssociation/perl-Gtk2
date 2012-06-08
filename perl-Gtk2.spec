%define upstream_name	Gtk2
%define	upstream_version 1.244

%define Werror_cflags %{nil}

%define perl_glib_require 1.233
%define gtk_require 2.24.10
%define cairo_require 1.00
%define pango_require 1.220

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl module for the gtk+-2.x library
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.gz
Patch7:		Gtk2-gtk_exit.patch
Patch21:	Gtk2-1.038-xset_input_focus.patch
Patch23:	Gtk2-1.023-exception-trapping.patch 
Patch24:	relocations-2.patch
Patch25:	relocations-fixes.patch

BuildRequires:	perl(Cairo) >= 1.0.0
BuildRequires:	perl(ExtUtils::Depends) >= 0.300.0
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.30.0
BuildRequires:	perl(Glib) >= 1.240.0
BuildRequires:	perl(Pango) >= 1.220.0
BuildRequires:	gtk+2-devel >= %{gtk_require}
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= %{perl_glib_require}
BuildRequires:	perl-Cairo >= %{cairo_require}
BuildRequires:	perl-Pango >= %{pango_require}
# for test suite:
BuildRequires:	fontconfig
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	x11-server-xvfb
Requires:	gtk+2
Requires:	libgtk+2 => %{gtk_require}
Requires:	perl-Glib >= %{perl_glib_require}
#	(misc) needed by /usr/lib/perl5/vendor_perl/5.8.7/i386-linux/Gtk2/Install/Files.pm
Requires:	perl-Cairo >= %{cairo_require}
Requires:	perl-Pango >= %{pango_require}
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
BuildArch:	noarch

%description	doc
This package contains documentation of the Gtk2 module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch7 -p0
%patch21 -p0 -b .tv
%patch23 -p0 -b .except
#%patch24 -p0 -b .reloc
#%patch25 -p0 -b .relocfix
perl Makefile.PL INSTALLDIRS=vendor
chmod 755 gtk-demo/*.pl examples/*.pl

%build
%make OPTIMIZE="%{optflags}"

%check
#xvfb-run %make test

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE META.yml NEWS README TODO examples
%{perl_vendorarch}/%{upstream_name}/
%{perl_vendorarch}/%{upstream_name}.pm
%exclude %{perl_vendorarch}/%{upstream_name}/*.pod
%exclude %{perl_vendorarch}/%{upstream_name}/*/*.pod
%exclude %{perl_vendorarch}/%{upstream_name}/*/*/*.pod
%{perl_vendorarch}/auto/*

%files doc
%doc gtk-demo examples
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{upstream_name}
%{perl_vendorarch}/%{upstream_name}/*.pod
%{perl_vendorarch}/%{upstream_name}/*/*.pod
%{perl_vendorarch}/%{upstream_name}/*/*/*.pod
