(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(base16-distinct-fringe-backgeround 0)
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
  (setq base16-theme-256-color-source 'base16-shell)
  (load "~/.emacs.d/base16-test")
  ;;(load-theme (quote base16-oceanicnext) t)
  )
(use-package doom-modeline
  :ensure t
  :hook (after-init . doom-modeline-mode)
  )
(use-package helm
  :config
  (helm-mode 1)
  (global-set-key (kbd "M-x") 'helm-M-x)
  )
(menu-bar-mode -1)
(custom-set-faces)
(eval-after-load "load-theme" '((concat "base16-" (getenv "BASE16_THEME")) t))
