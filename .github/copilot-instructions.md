# Polylab - Mathematical Dashboard Copilot Instructions

## Project Overview
Polylab is a mathematical visualization dashboard built with Dash and Plotly, featuring interactive polynomial and sinusoidal graphing with real-time coefficient manipulation. The app uses a modular tab-based architecture with dynamic theming and mathematical rendering via MathJax.

## Architecture Patterns

### Modular Organization
- **Tabs**: Each mathematical domain (polynomials, Hyperbolae, linear programming) is a separate module in `tabs/`
- **Callbacks**: Split between `callbacks.py` (core functionality) and `callbacks_cosmetics.py` (theme/UI state)
- **Components**: Reusable UI elements in `factory.py` and forms in `forms.py`
- **Defaults**: Configuration and styling in `defaults/` directory with organized submodules

### Core Application Flow
1. `app.py` - Main entry point, configures Dash app with MathJax integration
2. `layout.py` - Builds the app layout with theme switching and tab container
3. `callbacks.py` - Handles mathematical computations and graph updates
4. `callbacks_cosmetics.py` - Manages theme changes and UI cosmetics

### Key Classes and Patterns
- **MyPolynomial** (factory.py): Core mathematical class with NumPy polynomial integration
  - Handles coefficient-based polynomial creation, evaluation, and derivatives
  - Generates LaTeX-formatted titles with smart coefficient formatting rules
- **Theme Management**: Dual-theme system with `APP_THEMES` dict and dynamic stylesheet switching
- **Slider Factory**: `my_slider()` function creates consistent coefficient sliders with LaTeX labels

## Development Conventions

### Mathematical Rendering
- Use `dcc.Markdown(mathjax=True)` for LaTeX equations
- Follow the polynomial title formatting rules in `MyPolynomial.update_figure_title()`
- Store mathematical constants and notation in `defaults/mathematics.py`

### Styling and Theming
- All colors and styles centralized in `defaults/cosmetics.py`
- Use `STYLE_GRAPH_BORDER` for consistent graph styling
- Theme-aware color extraction from Plotly templates via `trace_colours` dict
- Bootstrap classes preferred over custom CSS

### Callback Patterns
- Use `Patch()` for efficient figure updates instead of returning entire figures
- Pattern matching IDs: `{"type": "polynomial_slider", "name": ALL}` for slider arrays
- Separate cosmetic callbacks from functional ones for maintainability
- Use `prevent_initial_call=True` for user-triggered interactions

### Component Organization
- Store reusable components in `factory.py` (graphs, sliders)
- Form controls in `forms.py` with consistent naming
- Modal definitions in `modals.py`
- Use `dbc.Stack()` for vertical component arrangements

## Critical Configuration

### Environment and Dependencies
- Uses `uv` for dependency management (pyproject.toml + uv.lock)
- Python 3.13+ required with specific Dash ecosystem versions
- MathJax CDN integration for mathematical rendering
- Development vs production mode controlled by `FLASK_DEBUG` environment variable

### File Structure Dependencies
- `defaults/` modules must maintain import relationships (cosmetics → mathematics → chart_elements)
- Tab modules import from factory and defaults consistently
- Assets stored in `assets/` directory (favicon, CSS)

## Running and Debugging
- Development: Set `FLASK_DEBUG=development` and run `python app.py`
- Hot reload enabled in development mode on port 8080
- Use `dash.Patch()` for debugging callback updates without full re-renders
- Theme switching affects both Bootstrap CSS and Plotly figure templates

## Key Files to Understand
- `factory.py`: Mathematical classes and component generators
- `defaults/cosmetics.py`: Complete theming and styling configuration
- `callbacks.py`: Core mathematical functionality and graph updates
- `layout.py`: App structure and theme integration