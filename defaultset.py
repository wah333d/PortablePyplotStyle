def plotrcset():
  import matplotlib
  from cycler import cycler

  font = {'family': 'Times New Roman',
          'weight': 'normal',
          'size': 6,
          'style': 'normal'}

  matplotlib.rc('font', **font)

  xtick = {'alignment': 'center',
           'color': 'black',
           'bottom': True,
           'direction': 'in',
           'labelbottom': True,
           'labelsize': 'medium',
           'labeltop': False,
           'major.bottom': True,
           'major.pad': 3.5,
           'major.size': 1.5,
           'major.top': True,
           'major.width': 0.4,
           'minor.bottom': True,
           'minor.pad': 3.4,
           'minor.size': 1.0,
           'minor.visible': False,
           'minor.width': 0.6,
           'top': True}

  ytick = {'alignment': 'center',
           'color': 'black',
           'left': True,
           'direction': 'in',
           'labelleft': True,
           'labelsize': 'medium',
           'labelleft': True,
           'major.left': True,
           'major.pad': 3.5,
           'major.size': 1.5,
           'major.right': True,
           'major.width': 0.4,
           'minor.left': True,
           'minor.pad': 3.4,
           'minor.size': 1.0,
           'minor.visible': False,
           'minor.width': 0.6,
           'right': True}

  axes = {'grid': False,
          'labelcolor': 'black',
          'labelpad': 4.0,
          'labelsize': 'medium',
          'labelweight': 'normal',
          'prop_cycle': cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']),
          'spines.bottom': True,
          'titlepad': 6.0,
          'titlesize': 'large',
          'titleweight': 'normal',
          'xmargin': 0.05,
          'ymargin': 0.05,
          'lw': 0.5}

  figure = {'edgecolor': 'black',
            'facecolor': 'white',
            'dpi': 300.0,
            'figsize': [6.4, 4.8],
            'titlesize': 'large',
            'titleweight': 'normal'}

  grid = {'alpha': 0.3,
          'color': 'b0b0b0',
          'linestyle': '-',
          'linewidth': 0.2}

  legend = {'facecolor': 'inherit',
            'markerscale': 1,
            'numpoints': 1,
            'loc': 'lower right',
            'shadow': False,
            'borderaxespad': 0.5,
            'borderpad': 0.4,
            'columnspacing': 2.0,
            'edgecolor': 'grey',
            'fontsize': 'medium',
            'framealpha': 0.4,
            'frameon': False,
            'handleheight': 0.7,
            'handlelength': 2.5,
            'handletextpad': 0.8,
            'labelspacing': 0.5,
            'scatterpoints': 1,
            'title_fontsize': None}

  text = {'color': 'black',
          'antialiased': True}

  lines = {'linestyle': '-',
           'linewidth': 1.0,
           'marker': None,
           'markeredgecolor': 'auto',
           'markeredgewidth': 1.0,
           'markerfacecolor': 'auto',
           'markersize': 1.0}

  markers = {'fillstyle': 'full'}

  mathtext = {'bf': 'sans:bold',
              'cal': 'cursive',
              'default': 'it',
              'fallback_to_cm': True,
              'fontset': 'dejavusans',
              'it': 'sans:italic',
              'rm': 'sans',
              'sf': 'sans',
              'tt': 'monospace'}

  patch = {'antialiased': True,
           'edgecolor': 'black',
           'facecolor': 'C0',
           'force_edgecolor': False,
           'linewidth': 1.0}

  savefig = {'bbox': None,
             'directory': '~',
             'dpi': 'figure',
             'edgecolor': 'white',
             'facecolor': 'white',
             'format': 'tiff',
             'frameon': True,
             'jpeg_quality': 95,
             'orientation': 'portrait',
             'pad_inches': 0.1,
             'transparent': False}

  scatter = {'marker': 'o'}

  matplotlib.rc('xtick', **xtick)
  matplotlib.rc('ytick', **ytick)
  matplotlib.rc('axes', **axes)
  matplotlib.rc('figure', **figure)
  matplotlib.rc('grid', **grid)
  matplotlib.rc('legend', **legend)
  matplotlib.rc('text', **text)
  matplotlib.rc('lines', **lines)
  matplotlib.rc('markers', **markers)
  matplotlib.rc('mathtext', **mathtext)
  matplotlib.rc('patch', **patch)
  matplotlib.rc('savefig', **savefig)
  matplotlib.rc('scatter', **scatter)
