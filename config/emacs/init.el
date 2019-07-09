(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(coding-system-for-read (quote utf-8) t)
 '(default-fill-column 80)
 '(delete-old-versions -1)
 '(delete-selection-mode nil)
 '(inhibit-startup-screen t)
 '(initial-scratch-message "Welcome in Emacs")
 '(ring-bell-function (quote ignore))
 '(sentence-end-double-space nil)
 '(version-control t)
 '(use-package-always-ensure t)
 )

(require 'package)
(add-to-list 'package-archives 
 '("melpa" . "https://melpa.org/packages/")
 '("gnu" . "http://elpa.gnu.org/packages/")
)

(package-initialize)

(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(require 'use-package)

(use-package evil
  :ensure t ;; install the evil package if not installed
  :init ;; tweak evil's configuration before loading it
  (setq evil-search-module 'evil-search)
  (setq evil-ex-complete-emacs-commands nil)
  (setq evil-vsplit-window-right t)
  (setq evil-split-window-below t)
  (setq evil-shift-round nil)
  (setq evil-want-C-u-scroll t)
  :config ;; tweak evil after loading it
  (evil-mode)
  )
;; base16 support
(use-package base16-theme
  :ensure t
  :init
  (setq base16-distinct-fringe-backgeround 0)
  (setq base16-theme-256-color-source 'base16-shell)
  (if (file-exists-p "~/.emacs_theme.el") 
      (load "~/.emacs_theme.el")
    )
  )
(use-package doom-modeline
  :ensure t
  :init
  (setq doom-modeline-icon t)
  (setq doom-modeline-major-mode-icon t)
  (setq doom-modeline-buffer-state-icon t)
  (setq doom-modeline-buffer-modification-icon t)
  (setq doom-modeline-minor-modes nil)
  (setq doom-modeline-enable-word-count nil)
  (setq doom-modeline-buffer-encoding t)
  (setq doom-modeline-indent-info nil)
  (setq doom-modeline-checker-simple-format t)
  (setq doom-modeline-vcs-max-length 12)
  (setq doom-modeline-persp-name t)
  (setq doom-modeline-persp-name-icon nil)
  (setq doom-modeline-lsp t)
  (setq doom-modeline-github nil)
  (setq doom-modeline-github-interval (* 30 60))
  (setq doom-modeline-env-version t)
  (setq doom-modeline-env-enable-python t)
  (setq doom-modeline-env-enable-ruby t)
  (setq doom-modeline-env-enable-perl t)
  (setq doom-modeline-env-enable-go t)
  (setq doom-modeline-env-enable-elixir t)
  (setq doom-modeline-env-enable-rust t)
  (setq doom-modeline-env-python-executable "python")
  (setq doom-modeline-env-ruby-executable "ruby")
  (setq doom-modeline-env-perl-executable "perl")
  (setq doom-modeline-env-go-executable "go")
  (setq doom-modeline-env-elixir-executable "iex")
  (setq doom-modeline-env-rust-executable "rustc")
  (setq doom-modeline-height 1)
  (set-face-attribute 'mode-line nil :height 100)
  (set-face-attribute 'mode-line-inactive nil :height 100)
  :hook (after-init . doom-modeline-mode)
  )
(use-package helm
  :config
  (helm-mode 1)
  (global-set-key (kbd "M-x") 'helm-M-x)
  )
(use-package all-the-icons)
(menu-bar-mode -1)
(custom-set-faces)
