 <svg viewBox="0 0 800 700" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="400" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#333">
    G1.2: Duality &amp; Dimensionality - Variables, Constraints, and Solution Spaces
  </text>
  
  <!-- Three panels for each formulation -->
  <!-- Panel 1: Primal (fix β) - Now with brown color -->
  <g transform="translate(50, 70)">
    <rect x="0" y="0" width="220" height="250" fill="#fdf5e6" stroke="#A0522D" stroke-width="2" rx="5"/>
    <text x="110" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#8B4513">
      Primal: Fix β
    </text>
    
    <!-- Variables -->
    <text x="10" y="50" font-size="14" font-weight="bold" fill="#333">Variables (3):</text>
    <text x="20" y="70" font-size="13" fill="#666">[q, βr, βc]ᵀ</text>
    
    <!-- Constraints -->
    <text x="10" y="95" font-size="14" font-weight="bold" fill="#333">Constraints (3):</text>
    <text x="20" y="112" font-size="12" fill="#666">βr = βr₀</text>
    <text x="20" y="128" font-size="12" fill="#666">βc = βc₀</text>
    <text x="20" y="144" font-size="11" fill="#666">q* = [Co(βc+βr)+Vβc]/</text>
    <text x="35" y="158" font-size="11" fill="#666">[2(Cuβc²+Coβrβc+Vβrβc)]</text>
    
    <!-- Matrix A -->
    <text x="10" y="180" font-size="14" font-weight="bold" fill="#333">Matrix A: 3×3</text>
    <g transform="translate(20, 185)">
      <rect x="0" y="0" width="180" height="50" fill="none" stroke="#999" stroke-width="1"/>
      <line x1="60" y1="0" x2="60" y2="50" stroke="#999" stroke-width="1"/>
      <line x1="120" y1="0" x2="120" y2="50" stroke="#999" stroke-width="1"/>
      <line x1="0" y1="17" x2="180" y2="17" stroke="#999" stroke-width="1"/>
      <line x1="0" y1="34" x2="180" y2="34" stroke="#999" stroke-width="1"/>
      <!-- Row 1 -->
      <text x="30" y="12" text-anchor="middle" font-size="11" fill="#333">0</text>
      <text x="90" y="12" text-anchor="middle" font-size="11" fill="#333">1</text>
      <text x="150" y="12" text-anchor="middle" font-size="11" fill="#333">0</text>
      <!-- Row 2 -->
      <text x="30" y="29" text-anchor="middle" font-size="11" fill="#333">0</text>
      <text x="90" y="29" text-anchor="middle" font-size="11" fill="#333">0</text>
      <text x="150" y="29" text-anchor="middle" font-size="11" fill="#333">1</text>
      <!-- Row 3 (newsvendor constraint) -->
      <text x="30" y="46" text-anchor="middle" font-size="11" fill="#333">1</text>
      <text x="90" y="46" text-anchor="middle" font-size="11" fill="#333">f₁</text>
      <text x="150" y="46" text-anchor="middle" font-size="11" fill="#333">f₂</text>
    </g>
    
    <!-- Solution Space -->
    <text x="10" y="290" font-size="14" font-weight="bold" fill="#333">Solution: 0D point</text>
    <text x="10" y="305" font-size="12" fill="#666">(newsvendor solution)</text>
  </g>
  
  <!-- Panel 2: Dual (fix q) - Now with skyblue color -->
  <g transform="translate(290, 70)">
    <rect x="0" y="0" width="220" height="250" fill="#f0f8ff" stroke="#87CEEB" stroke-width="2" rx="5"/>
    <text x="110" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#4682B4">
      Dual: Fix q
    </text>
    
    <!-- Variables -->
    <text x="10" y="50" font-size="14" font-weight="bold" fill="#333">Variables (3):</text>
    <text x="20" y="70" font-size="13" fill="#666">[q, βr, βc]ᵀ</text>
    
    <!-- Constraints -->
    <text x="10" y="95" font-size="14" font-weight="bold" fill="#333">Constraints (1):</text>
    <text x="20" y="112" font-size="13" fill="#666">q = q₀</text>
    
    <!-- Matrix A -->
    <text x="10" y="180" font-size="14" font-weight="bold" fill="#333">Matrix A: 1×3</text>
    <g transform="translate(20, 185)">
      <rect x="0" y="0" width="180" height="20" fill="none" stroke="#999" stroke-width="1"/>
      <line x1="60" y1="0" x2="60" y2="20" stroke="#999" stroke-width="1"/>
      <line x1="120" y1="0" x2="120" y2="20" stroke="#999" stroke-width="1"/>
      <text x="30" y="15" text-anchor="middle" font-size="11" fill="#333">1</text>
      <text x="90" y="15" text-anchor="middle" font-size="11" fill="#333">0</text>
      <text x="150" y="15" text-anchor="middle" font-size="11" fill="#333">0</text>
    </g>
    
    <!-- Solution Space -->
    <text x="10" y="290" font-size="14" font-weight="bold" fill="#333">Solution: 2D plane</text>
    <text x="10" y="305" font-size="12" fill="#666">(predict responsiveness)</text>
  </g>
  
  <!-- Panel 3: Integrated (all free) -->
  <g transform="translate(530, 70)">
    <rect x="0" y="0" width="220" height="250" fill="#f0fff0" stroke="#228b22" stroke-width="2" rx="5"/>
    <text x="110" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#228b22">
      Integrated: All Free
    </text>
    
    <!-- Variables -->
    <text x="10" y="50" font-size="14" font-weight="bold" fill="#333">Variables (3):</text>
    <text x="20" y="70" font-size="13" fill="#666">[q, βr, βc]ᵀ</text>
    
    <!-- Constraints -->
    <text x="10" y="95" font-size="14" font-weight="bold" fill="#333">Constraints (1):</text>
    <text x="20" y="112" font-size="11" fill="#666">q* = [Co(βc+βr)+Vβc]/</text>
    <text x="35" y="126" font-size="11" fill="#666">[2(Cuβc²+Coβrβc+Vβrβc)]</text>
    <text x="20" y="142" font-size="12" fill="#666">(optimality condition)</text>
    
    <!-- Matrix A -->
    <text x="10" y="180" font-size="14" font-weight="bold" fill="#333">Matrix A: 1×3</text>
    <g transform="translate(20, 185)">
      <rect x="0" y="0" width="180" height="20" fill="none" stroke="#999" stroke-width="1"/>
      <line x1="60" y1="0" x2="60" y2="20" stroke="#999" stroke-width="1"/>
      <line x1="120" y1="0" x2="120" y2="20" stroke="#999" stroke-width="1"/>
      <text x="30" y="15" text-anchor="middle" font-size="11" fill="#333">1</text>
      <text x="90" y="15" text-anchor="middle" font-size="11" fill="#333">g₁</text>
      <text x="150" y="15" text-anchor="middle" font-size="11" fill="#333">g₂</text>
    </g>
    
    <!-- Solution Space -->
    <text x="10" y="290" font-size="14" font-weight="bold" fill="#333">Solution: 2D surface</text>
    <text x="10" y="305" font-size="12" fill="#666">(optimal manifold)</text>
  </g>
  
  <!-- Visual representations of solution spaces -->
  <g transform="translate(50, 370)">
    <!-- 0D point (Primal) -->
    <text x="110" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#8B4513">0D Point</text>
    <g transform="translate(60, 30)">
      <!-- 3D axes -->
      <line x1="50" y1="50" x2="10" y2="80" stroke="#ccc" stroke-width="1"/>
      <line x1="50" y1="50" x2="90" y2="80" stroke="#ccc" stroke-width="1"/>
      <line x1="50" y1="50" x2="50" y2="10" stroke="#ccc" stroke-width="1"/>
      <text x="5" y="85" font-size="10" fill="#999">βᵣ</text>
      <text x="95" y="85" font-size="10" fill="#999">βc</text>
      <text x="45" y="8" font-size="10" fill="#999">q</text>
      <!-- Solution point -->
      <circle cx="50" cy="50" r="5" fill="#A0522D" stroke="#8B4513" stroke-width="2"/>
      <text x="60" y="55" font-size="10" fill="#8B4513">q*</text>
    </g>
  </g>
  
  <g transform="translate(290, 370)">
    <!-- 2D plane (Dual) -->
    <text x="110" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#4682B4">2D Plane</text>
    <g transform="translate(60, 30)">
      <!-- 3D axes -->
      <line x1="50" y1="50" x2="10" y2="80" stroke="#ccc" stroke-width="1"/>
      <line x1="50" y1="50" x2="90" y2="80" stroke="#ccc" stroke-width="1"/>
      <line x1="50" y1="50" x2="50" y2="10" stroke="#ccc" stroke-width="1"/>
      <text x="5" y="85" font-size="10" fill="#999">βᵣ</text>
      <text x="95" y="85" font-size="10" fill="#999">βc</text>
      <text x="45" y="8" font-size="10" fill="#999">q</text>
      <!-- Solution plane -->
      <path d="M 20,60 L 80,60 L 100,40 L 40,40 Z" fill="#87CEEB" fill-opacity="0.3" stroke="#4682B4" stroke-width="2"/>
      <circle cx="50" cy="50" r="4" fill="#4682B4"/>
    </g>
  </g>
  
  <g transform="translate(530, 370)">
    <!-- 2D surface (Integrated) -->
    <text x="110" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#228b22">2D Surface</text>
    <g transform="translate(60, 30)">
      <!-- 3D axes -->
      <line x1="50" y1="50" x2="10" y2="80" stroke="#ccc" stroke-width="1"/>
      <line x1="50" y1="50" x2="90" y2="80" stroke="#ccc" stroke-width="1"/>
      <line x1="50" y1="50" x2="50" y2="10" stroke="#ccc" stroke-width="1"/>
      <text x="5" y="85" font-size="10" fill="#999">βᵣ</text>
      <text x="95" y="85" font-size="10" fill="#999">βc</text>
      <text x="45" y="8" font-size="10" fill="#999">q</text>
      <!-- Solution surface (curved) -->
      <path d="M 20,55 Q 50,30 80,55 L 95,45 Q 50,20 25,45 Z" 
            fill="#228b22" fill-opacity="0.3" stroke="#228b22" stroke-width="2"/>
      <circle cx="50" cy="40" r="4" fill="#228b22"/>
    </g>
  </g>
  
  <!-- Key insights -->
  <rect x="50" y="520" width="700" height="120" fill="#f5f5f5" stroke="#333" stroke-width="2" rx="5"/>
  <text x="400" y="545" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">
    Key Insights: Degrees of Freedom = Variables - rank(A)
  </text>
  <text x="400" y="565" text-anchor="middle" font-size="13" fill="#333">
    Primal: 3 - 3 = 0D (unique newsvendor solution) | Dual: 3 - 1 = 2D | Integrated: 3 - 1 = 2D
  </text>
  <text x="400" y="585" text-anchor="middle" font-size="12" fill="#666">
    Primal: Prescription-only (given β, find optimal q via newsvendor)
  </text>
  <text x="400" y="600" text-anchor="middle" font-size="12" fill="#666">
    Dual: Prediction-only (given q, observe/predict stakeholder responsiveness)
  </text>
  <text x="400" y="615" text-anchor="middle" font-size="12" fill="#666">
    Integrated: Strategic choice (optimize q understanding market structure β)
  </text>
  <text x="400" y="630" text-anchor="middle" font-size="11" fill="#333">
    The four cases (symmetric, customer/partner-dominant, high-match) are all integrated solutions
  </text>
</svg>