-- Initialize ArchiOps Database
-- Multiple databases for different architecture aspects

-- Create additional databases if they don't exist
SELECT 'CREATE DATABASE projects'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'projects')\gexec

SELECT 'CREATE DATABASE bim'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'bim')\gexec

SELECT 'CREATE DATABASE designs'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'designs')\gexec

SELECT 'CREATE DATABASE portfolios'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'portfolios')\gexec

SELECT 'CREATE DATABASE metabase'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'metabase')\gexec

SELECT 'CREATE DATABASE gitea'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'gitea')\gexec

-- Connect to archiops database and create initial schema
\c archiops;

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Create architecture projects table
CREATE TABLE IF NOT EXISTS architecture_projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL, -- building, software, enterprise, solution, system
    client VARCHAR(255),
    status VARCHAR(50) DEFAULT 'planning',
    budget DECIMAL(15, 2),
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create architects table
CREATE TABLE IF NOT EXISTS architects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    specialty VARCHAR(100), -- building, software, enterprise, solution, system
    license_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create architecture documents table
CREATE TABLE IF NOT EXISTS architecture_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES architecture_projects(id),
    title VARCHAR(255) NOT NULL,
    document_type VARCHAR(50), -- diagram, blueprint, specification, adr
    file_path TEXT,
    version VARCHAR(20),
    created_by UUID REFERENCES architects(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create design reviews table
CREATE TABLE IF NOT EXISTS design_reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID REFERENCES architecture_documents(id),
    reviewer_id UUID REFERENCES architects(id),
    status VARCHAR(50) DEFAULT 'pending', -- pending, approved, rejected, revision_requested
    comments TEXT,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_projects_type ON architecture_projects(type);
CREATE INDEX IF NOT EXISTS idx_projects_status ON architecture_projects(status);
CREATE INDEX IF NOT EXISTS idx_documents_project ON architecture_documents(project_id);
CREATE INDEX IF NOT EXISTS idx_reviews_document ON design_reviews(document_id);

-- Create full-text search index
CREATE INDEX IF NOT EXISTS idx_projects_name_trgm ON architecture_projects USING gin(name gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_documents_title_trgm ON architecture_documents USING gin(title gin_trgm_ops);

-- Insert sample data
INSERT INTO architects (name, email, specialty) VALUES
    ('Jane Smith', 'jane.smith@archiops.com', 'building'),
    ('John Doe', 'john.doe@archiops.com', 'software'),
    ('Alice Johnson', 'alice.j@archiops.com', 'enterprise')
ON CONFLICT (email) DO NOTHING;
