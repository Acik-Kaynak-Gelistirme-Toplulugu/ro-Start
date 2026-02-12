%global _version 2.0.0

Name:           ro-start
Version:        %{_version}
Release:        1%{?dist}
Summary:        Fast, safe, and beautiful Linux welcome application

License:        GPL-3.0-or-later
URL:            https://github.com/Acik-Kaynak-Gelistirme-Toplulugu/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  rust >= 1.70
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  gtk4-devel >= 4.12
BuildRequires:  libadwaita-devel >= 1.5

Requires:       gtk4 >= 4.12
Requires:       libadwaita >= 1.5

%description
Ro-Start is a modern welcome application for Linux distributions built with
Rust and GTK4. It provides system information, update checking, and quick
actions for new users with a native GNOME experience.

Features:
- Lightning-fast startup (~0.5 seconds)
- Minimal memory usage (~45 MB RAM)
- Native GTK4 + libadwaita interface
- Memory-safe Rust implementation
- 9 language support
- Package manager integration (apt, dnf, pacman, zypper)

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

%install
# Install binary
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Install desktop files
install -Dm644 data/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 data/%{name}-autostart.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

# Install icon
install -Dm644 data/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

# Install AppData
install -Dm644 data/org.osdev.ro_start.appdata.xml %{buildroot}%{_datadir}/metainfo/org.osdev.ro_start.appdata.xml

# Install man page
install -Dm644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Install shell completions
install -Dm644 packaging/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 packaging/completions/%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 packaging/completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# Install documentation
install -Dm644 README.md %{buildroot}%{_docdir}/%{name}/README.md

%check
cargo test --release

%post
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/metainfo/org.osdev.ro_start.appdata.xml
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_docdir}/%{name}/README.md

%changelog
* Thu Feb 13 2026 Açık Kaynak Geliştirme Topluluğu <info@osdev.shop> - 2.0.0-1
- Version 2.0.0 Release
- Complete rewrite in Rust + GTK4
- Native GNOME integration with libadwaita
- 5x faster startup compared to previous versions
- 4.4x reduced memory footprint
- Memory-safe implementation
- Single binary distribution
- Full i18n support (9 languages)
- Package manager integration (apt, dnf, pacman, zypper)
- System information display
